import sys
import time
import csv
import praw
import requests
from datetime import datetime, timezone
from typing import List, Dict
import json
import os

# === Hardcoded Reddit API credentials ===
REDDIT_CLIENT_ID = 'QPAItQzJ0x7H3MOpj7BCcA'  # Your Client ID
REDDIT_CLIENT_SECRET = 'fFW1Dgik95qmfhzD9rCzkPrdXuHfpg'  # Your Client Secret
REDDIT_USER_AGENT = 'Destroying_Angel_Snuferno'

# === Hardcoded OpenRouter API settings ===
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Batch size for OpenRouter API calls
BATCH_SIZE = 20


def authenticate_reddit():
    """Authenticate and return a Reddit instance."""
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    return reddit


def fetch_reddit_data(reddit, keyword: str, limit: int = 500) -> List[Dict]:
    """
    Fetch Reddit posts and comments matching the keyword.
    Returns a list of dicts with required fields.
    """
    results = []
    count = 0

    # Search submissions with the keyword in all subreddits
    submissions = reddit.subreddit('all').search(keyword, limit=None)

    for submission in submissions:
        if count >= limit:
            break

        # Add submission as a post
        results.append({
            'id': count + 1,
            'topic': keyword,
            'text': submission.title + ("\n" + submission.selftext if submission.selftext else ""),
            'timestamp': datetime.fromtimestamp(submission.created_utc, timezone.utc).isoformat(),
            'source': 'manual input',
            'notes': '',
            'username': str(submission.author) if submission.author else 'unknown',
            'upvotes': submission.score,
            'type': 'post'
        })
        count += 1

        # Fetch comments for this submission
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if count >= limit:
                break
            results.append({
                'id': count + 1,
                'topic': keyword,
                'text': comment.body,
                'timestamp': datetime.fromtimestamp(comment.created_utc, timezone.utc).isoformat(),
                'source': 'manual input',
                'notes': '',
                'username': str(comment.author) if comment.author else 'unknown',
                'upvotes': comment.score,
                'type': 'comment'
            })
            count += 1

    return results[:limit]


def build_openrouter_prompt(batch: List[Dict]) -> List[Dict]:
    """
    Build the messages payload for OpenRouter API chat completion.
    Includes text plus upvotes for context.
    """
    system_message = {
        "role": "system",
        "content": (
            "You are a sentiment analysis assistant. For each text, classify the sentiment as Positive, Negative, or Neutral. "
            "Provide a confidence score between 0 and 1. Use the upvotes as additional context but base your classification primarily on the text content. "
            "Respond ONLY with a JSON array of objects with 'sentiment' and 'score' fields, in the same order as the texts."
        )
    }

    user_texts = []
    for i, item in enumerate(batch):
        upvotes = item['upvotes'] if item['upvotes'] is not None else 0
        user_texts.append(
            f"Text {i+1}: {item['text']}\nUpvotes: {upvotes}"
        )

    user_message = {
        "role": "user",
        "content": "\n\n".join(user_texts) + "\n\nPlease respond with a JSON array of sentiment objects."
    }

    return [system_message, user_message]


def call_openrouter_api(batch: List[Dict]) -> List[Dict]:
    """
    Call OpenRouter API to get sentiment classification for a batch of texts.
    Returns a list of dicts with sentiment and sentiment_score for each text.
    """
    headers = {
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'Content-Type': 'application/json'
    }

    messages = build_openrouter_prompt(batch)

    payload = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0
    }

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()

    assistant_message = data['choices'][0]['message']['content']

    # Debug print to see raw model output for troubleshooting
    print("Raw model response:", assistant_message)

    # Clean the response by removing markdown code fences if present
    cleaned_response = assistant_message.strip()
    if cleaned_response.startswith("```"):
        # Remove the first line (```json or ```), and the last line (```)
        lines = cleaned_response.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned_response = "\n".join(lines).strip()

    try:
        sentiment_results = json.loads(cleaned_response)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        # Fallback: assign neutral sentiment
        sentiment_results = [{"sentiment": "Neutral", "score": 0.5} for _ in batch]

    return sentiment_results


def batch_process_sentiment(data: List[Dict]) -> List[Dict]:
    """
    Process the data in batches through OpenRouter API and add sentiment results.
    """
    all_results = []
    total_batches = (len(data) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, len(data), BATCH_SIZE):
        batch_num = i // BATCH_SIZE + 1
        batch = data[i:i+BATCH_SIZE]
        print(f"Processing batch {batch_num} of {total_batches} with {len(batch)} items...")

        try:
            sentiments = call_openrouter_api(batch)
        except Exception as e:
            print(f"Error calling OpenRouter API: {e}")
            sentiments = [{"sentiment": "Neutral", "score": 0.5} for _ in batch]

        timestamp = datetime.now(timezone.utc).isoformat()
        for idx, (item, sentiment) in enumerate(zip(batch, sentiments), start=1):
            item['sentiment'] = sentiment.get('sentiment', 'Neutral')
            item['sentiment_score'] = sentiment.get('score', None)
            item['timestamp'] = timestamp
            all_results.append(item)
            print(f"  Processed item {idx} in batch {batch_num}: Sentiment={item['sentiment']}, Score={item['sentiment_score']}")

        time.sleep(1)  # To respect rate limits

    return all_results


def generate_output_filename(keyword: str) -> str:
    """
    Generate a dynamic filename like supersnu(keywordXXX).csv where XXX is a 3-digit incremental ID.
    """
    base_name = f"supersnu({keyword})"
    existing_files = [f for f in os.listdir('.') if f.startswith(base_name) and f.endswith('.csv')]
    existing_ids = []
    for f in existing_files:
        try:
            num = int(f[len(base_name):-4])
            existing_ids.append(num)
        except:
            pass
    next_id = max(existing_ids) + 1 if existing_ids else 1
    return f"{base_name}{str(next_id).zfill(3)}.csv"


def save_to_csv(data: List[Dict], filename: str):
    """
    Save the processed data to a CSV file with specified columns.
    """
    fieldnames = [
        'id', 'topic', 'text', 'sentiment', 'sentiment_score', 'timestamp',
        'source', 'notes', 'username', 'upvotes', 'type'
    ]
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 sentiment_analysis_openroutersupersnu.py \"KEYWORD\"")
        sys.exit(1)

    keyword = sys.argv[1]
    print(f"Fetching Reddit data for keyword: {keyword}")

    reddit = authenticate_reddit()
    reddit_data = fetch_reddit_data(reddit, keyword, limit=500)
    print(f"Fetched {len(reddit_data)} posts/comments from Reddit.")

    print("Analyzing sentiment with OpenRouter API in batches...")
    analyzed_data = batch_process_sentiment(reddit_data)

    output_file = generate_output_filename(keyword)
    save_to_csv(analyzed_data, output_file)
    print(f"Sentiment analysis results saved to {output_file}")


if __name__ == "__main__":
    main()
