# gemini_reddit_analyzer.py

---
[TEST PROJECT](https://docs.google.com/spreadsheets/d/11V__bxurXwEG23HJdENZdlPvy8ZaOWDwOlkjBjat9Hw/edit?usp=sharing)
---
[INITIAL WORKING CODE](https://github.com/cullenmccutcheon/Data-Projects-TripleTen/blob/main/Openrouter%20Integrated%20Python3%20Sentiment%20Analyzer/sentiment_analysis_openrouter.py)
---
[FINAL WORKING CODE](https://github.com/cullenmccutcheon/Data-Projects-TripleTen/tree/main/Openrouter%20Integrated%20Python3%20Sentiment%20Analyzer#:~:text=3%20days%20ago-,gemini_reddit_analyzer.py,-Create%20gemini_reddit_analyzer.py)
---
Contextual definitions:
- ***Iteratively refining the prompt:*** means making small changes to the instructions you give the AI, testing how it responds, and then adjusting those instructions again and again until the AI gives better and more accurate answers.

## Project Description

Supersnu is a Python-based sentiment analysis application I developed with the goal of building an effective and practical tool for analyzing public opinion on social media. My idea was to create an integration that fetches Reddit posts and comments related to any keyword, then uses advanced natural language processing via the OpenRouter API to classify the sentiment of these texts. This project serves a dual purpose: not only to deepen my understanding of API integration, prompt engineering, and data processing, but also to generate real-world insights that can be applied to companies I am interested in working for. By researching and analyzing sentiment around these companies or their products, I aim to build a portfolio project that demonstrates my technical skills and analytical capabilities, ultimately impressing future employers and opening doors to career opportunities.

The project involves:

- Authenticating and querying Reddit for posts and comments matching a keyword
- Processing the collected data in batches for sentiment classification via OpenRouter’s GPT-based API
- Handling API responses and saving enriched data with sentiment scores to CSV files
- Implementing robust error handling and progress tracking for large datasets

## Executive Summary

Supersnu was developed through an iterative process leveraging AI assistance to build a reliable and efficient sentiment analysis pipeline. The tool integrates Reddit’s API for data collection and OpenRouter’s GPT-4o-mini model for sentiment classification. Key challenges addressed include managing API rate limits, ensuring accurate sentiment extraction, and refining prompts to improve model output quality.

The project highlights:

1. Data Collection: Using PRAW (Python Reddit API Wrapper) to fetch relevant posts and comments, ensuring comprehensive coverage of the keyword across Reddit.
2. Sentiment Analysis: Crafting precise prompts for the OpenRouter API to classify sentiment as Positive, Negative, or Neutral, with confidence scores.
3. Troubleshooting & Optimization: Removing irrelevant data points (like downvotes), enhancing prompt clarity, and adding detailed logging to monitor batch processing and API responses.
4. Output Management: Dynamically generating output filenames and saving results in a structured CSV format for easy analysis.

## Detailed Problem Solving and Successes

Throughout the development of Supersnu, I encountered several technical challenges that required careful problem solving:

- **JSON Parsing Issues:** The OpenRouter API sometimes returned responses wrapped in markdown code fences or with unexpected formatting, causing JSON parsing errors. To solve this, I prompted the Route LLM to implemented logic that detected and stripped these code fences before attempting to parse the JSON, ensuring robust handling of API responses.
- **Fallback Handling:** When JSON parsing failed, the script gracefully fell back to assigning a neutral sentiment with a confidence score of 0.5, preventing crashes and allowing batch processing to continue uninterrupted.
- **Prompt Refinement:** Initial prompts led to overly neutral sentiment classifications, By iteratively refining the prompt to emphasize text content over metadata like upvotes, and by removing misleading fields such as downvotes (which Reddit does not provide), the model produced more nuanced and accurate sentiment results.
- **Batch Processing with Progress Logging:** To handle large datasets without hitting API rate limits, I implemented batch processing with detailed console logging. This provided real-time feedback on processing progress and sentiment results, aiding debugging and performance monitoring.
- **Automated Output Management:** The script dynamically generates output filenames to avoid overwriting previous results, and saves data in a clean CSV format with all relevant fields for further analysis.

  ***Image of code for fallback handling and Batch processing***

This iterative troubleshooting and refinement process, supported by AI assistance, was crucial in transforming Supersnu from a basic prototype into a robust and user-friendly sentiment analysis tool.

This partnership allowed me to focus on the project’s goals while leveraging AI expertise to overcome technical hurdles, resulting in a robust and user-friendly sentiment analysis tool.

---

### Sample Batch Processing Output

***Add Images of initial, mid, and post processing output***

## Results

The tool successfully fetched and analyzed hundreds of Reddit posts and comments, providing sentiment labels and confidence scores for each. Initial runs showed purely neutral classifications, which was addressed by refining the prompt and removing misleading data such as downvotes. The final version delivers nuanced sentiment insights that can be used for market research, social listening, or academic studies.

## Conclusions

Supersnu demonstrates how combining open-source APIs and AI models can create powerful tools for social media sentiment analysis. The project underscores the importance of prompt engineering, data preprocessing, and iterative debugging when working with language models. By automating sentiment classification on Reddit data, Supersnu offers a scalable solution for understanding public opinion on any topic.

## Recommendations

Future improvements could include:

- Incorporating more metadata (e.g., subreddit info, post flair) to enrich context
- Experimenting with different models or temperature settings for varied outputs
- Adding visualization dashboards to present sentiment trends over time
- Expanding support to other social media platforms for broader analysis

---

## How I Built Supersnu with AI Assistance

Building Supersnu was a collaborative journey with an AI assistant that helped me navigate the complexities of API integration and error handling. Although I had a foundational understanding of Python and APIs, the AI guided me through best practices and troubleshooting steps that accelerated development.

Together, we:

- Structured the Reddit data fetching logic using PRAW, ensuring efficient retrieval of posts and comments.
- Designed and refined prompts for the OpenRouter GPT model to improve sentiment classification accuracy.
- Implemented batch processing with progress updates to handle large datasets without hitting rate limits.
- Debugged JSON parsing issues by adding detailed logging of raw API responses.
- Simplified the input data by removing unnecessary fields like downvotes, which improved model performance.
- Automated output file naming and CSV saving for organized result management.

This partnership allowed me to focus on the project’s goals while leveraging AI expertise to overcome technical hurdles and do the grunt work, resulting in a robust and user-friendly sentiment analysis tool.
