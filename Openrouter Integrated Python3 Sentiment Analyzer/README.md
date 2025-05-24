# gemini_reddit_analyzer.py

---
[TEST PROJECT](https://docs.google.com/spreadsheets/d/1c9ot8IctNxoTVLcKLSTYXErUiSXgOKOyVCYxSjoJQzk/edit?usp=sharing)
---
[INITIAL CONCEPT CODE (OpenRouter based)](https://github.com/cullenmccutcheon/Data-Projects-TripleTen/blob/main/Openrouter%20Integrated%20Python3%20Sentiment%20Analyzer/sentiment_analysis_openrouter.py)
---
[FINAL WORKING CODE (Gemini API based)](https://github.com/cullenmccutcheon/Data-Projects-TripleTen/blob/main/Openrouter%20Integrated%20Python3%20Sentiment%20Analyzer/gemini_reddit_analyzer.py)
---
[TRY IT OUT!](https://www.notion.so/gemini_reddit_analyzer-py-1fc3e0a1c7c4809babf9dd0c4eb73ddd?pvs=4)
---
Contextual definitions:
- ***Iteratively refining the prompt:*** means making small changes to the instructions you give the AI, testing how it responds, and then adjusting those instructions again and again until the AI gives better and more accurate answers.

## Project Description

Supersnu is a Python-based sentiment analysis application conceived to provide effective and practical tools for analyzing public opinion on social media. The core idea was to develop an integration that fetches Reddit posts and comments related to any given keyword. I was intially running my data through Openrouter, afer some solid advice Google's Gemini API took it's place. This project serves a dual purpose: to deepen my expertise in API integration, sophisticated prompt engineering, complex data processing, and to generate tangible, real-world insights. By researching and analyzing sentiment around $TSLA, the aim is to build a compelling portfolio piece that showcases my ability to problem solve, adapt and achieve results even when I might be in over my head. Despite walking into this process with little to no knowlege of sentiment analysis, after a few weeks of research and troubleshooting I was able to leverage AI and build an effective and relevant tool.

The project encompasses:

- Authenticating and querying Reddit for posts and comments matching a keyword using PRAW.
- Securely managing API credentials through environment variables, a best practice in application development.
- Processing collected data in batches for sentiment classification via Google's Gemini API.
- Engineering highly effective prompts for the Gemini API to ensure precise sentiment classification and structured JSON output.
- Implementing sophisticated handling of API responses, including robust JSON parsing and comprehensive error management.
- Saving enriched data, complete with sentiment scores, to dynamically named CSV files for organized data stewardship.
- Incorporating robust error handling and clear progress tracking mechanisms suitable for large datasets.

## Executive Summary

Supersnu was engineered through an iterative development cycle, significantly enhanced by AI-assisted methodologies, resulting in a reliable and efficient sentiment analysis pipeline. The tool masterfully integrates Reddit’s API for data acquisition. Following initial research with OpenRouter, the sentiment classification component was strategically transitioned to Google's Gemini API (specifically 'gemini-2.5-flash-preview-04-17'). Key engineering achievements include a seamless migration of API integrations, the secure and effective management of environment variables, resolution of complex Python script execution issues, and the iterative refinement of prompts to ensure high-fidelity sentiment analysis.

The project highlights:

1.  **Advanced Data Collection:** Utilizing PRAW (Python Reddit API Wrapper) to comprehensively fetch relevant posts and comments for any keyword across Reddit.
2.  **Secure and Modern API Usage:** Transitioning from potentially insecure hardcoded credentials to a best-practice approach using environment variables for both Reddit and Gemini APIs. This involved mastering secure setup for terminal sessions and Python script access.
3.  **High-Fidelity Sentiment Analysis with Gemini:** Designing and fine-tuning precise prompts for the Gemini API to accurately classify sentiment (Positive, Negative, Neutral) with accompanying confidence scores, while ensuring the output is consistently in a parseable JSON format.
4.  **Systematic Troubleshooting & Optimization:** Methodically addressing and overcoming a range of technical challenges, including `FileNotFoundError`, `ModuleNotFoundError`, `NameError` related to environment variable configurations, and shell-specific `zsh: bad assignment` errors. This involved meticulous debugging and refinement of the Python script and terminal command configurations.
5.  **Streamlined Output Management:** Implementing dynamic generation of output filenames and structuring results in CSV format, now systematically saved to a dedicated `output_csvs` directory for improved project organization.

## Detailed Problem Solving and Engineering Successes

The development of Supersnu, especially the strategic migration to and robust implementation of the Gemini API, presented a series of engineering challenges that were systematically addressed:

-   **Strategic API Selection and Adaptation:** The project initially explored OpenRouter. However, to enhance robustness and leverage more advanced NLP capabilities, a strategic decision was made to transition to the Gemini API. This necessitated a thoughtful re-architecture of API call logic, prompt engineering strategies, and response handling mechanisms.

-   **Implementing Secure and Flexible Configuration:**
    *   **Enhanced Security:** A key architectural improvement was moving from hardcoded API credentials to the industry-standard use of environment variables for both Reddit and Gemini keys.
    *   **Environment Synchronization:** Ensured correct terminal setup for environment variables (e.g., `EXPORT VAR_NAME='value'` without spaces for zsh) and precise Python script configuration to access these variables (e.g., `os.environ.get('API_KEY')` by using the variable *name* `API_KEY` stored in `ENV_GEMINI_API_KEY`).
    *   **Resolving NameErrors:** Corrected initial misconfigurations in the Python script where global variables meant to store the *names* of environment keys were mistakenly assigned credential values directly. Ensuring these global variables correctly held strings like `'REDDIT_CLIENT_ID'` enabled proper lookup.

-   **Ensuring Robust Script Portability and Execution:**
    *   Addressed `[Errno 2] No such file or directory` errors by standardizing script execution, either by navigating to the script's directory (`cd Desktop`) or by using its full path, ensuring findability.

-   **Managing Project Dependencies for a Stable Environment:**
    *   Resolved `ModuleNotFoundError: No module named 'google.generativeai'` by integrating `pip3 install google-generativeai` (and `praw`) into the setup process, ensuring all necessary libraries were available to the Python interpreter.

-   **Advanced JSON Parsing from Gemini API:** Engineered the Gemini API interaction to return JSON. Developed resilient parsing logic, including stripping potential markdown code fences (e.g., ```json ... ```) from API responses, to ensure reliable data extraction.

-   **Building Inherent Script Robustness & Fallbacks:** In instances of Gemini API call failures or malformed JSON responses (even after retries), the script was architected to gracefully assign a "Neutral" sentiment and a 0.5 score, logging the error. This design choice ensures continuous batch processing without interruption. Added validation for individual items within the returned JSON array.

-   **Sophisticated Prompt Engineering for Gemini:** The prompt for the Gemini API (`build_gemini_batch_prompt`) was meticulously engineered to request specific sentiment categories (Positive, Negative, Neutral) and a confidence score, with an explicit directive for JSON array output. This level of iterative refinement is key to achieving consistent, high-quality structured data from large language models.

-   **Efficient Batch Processing and Rate Limit Management:** To process large Reddit datasets effectively while respecting API rate limits, the script employs batching (batch size optimized for Gemini's prompt length considerations). A `time.sleep(1)` delay between batch calls and a retry mechanism (up to 3 retries) for API calls were implemented to handle transient network conditions.

-   **Organized Data Output:** The `generate_output_filename` function was enhanced to save CSV files into a dedicated `output_csvs` subdirectory, promoting a cleaner project structure.

This structured approach to problem-solving, leveraging AI assistance as a powerful tool for complex integrations and debugging, was instrumental in evolving Supersnu into a highly functional and robust sentiment analysis application.

---

### Sample Batch Processing Output

*(This is where I'd insert screenshots of the terminal output during a successful run of `gemini_reddit_analyzer.py`, showing messages like "Fetching Reddit data...", "Successfully authenticated with Reddit.", "Processing batch X of Y...", "Processed item X/Y: Sentiment=..., Score=...", and finally "Sentiment analysis results saved to output_csvs/supersnu(Keyword)XXX.csv")*

---

## Results

Following a rigorous development and debugging phase, the `gemini_reddit_analyzer.py` tool now capably fetches Reddit data for specified keywords, processes it efficiently in batches using the Gemini API, and performs accurate sentiment analysis. The script demonstrates best practices in API key management via environment variables, handles Python dependencies correctly, and robustly parses JSON responses from the Gemini API. The final output is a well-structured CSV file, saved to an `output_csvs` directory, containing the original Reddit data enriched with sentiment labels (Positive, Negative, Neutral) and confidence scores. This data is immediately usable for in-depth analysis or for import into other analytical platforms like Google Sheets.

## Conclusions

Supersnu stands as a testament to how the strategic combination of Reddit's API and advanced AI models like Google's Gemini API can yield powerful tools for social media sentiment analysis. The project underscores the critical importance of:
1.  Secure and professional management of API keys using environment variables.
2.  Diligent configuration of the local development environment, encompassing Python package installations and precise terminal command syntax.
3.  Careful Python script architecture, especially concerning global variable definitions and their functional scope.
4.  Strategic prompt engineering for LLMs to ensure structured, accurate, and reliable responses.
5.  An iterative engineering approach, augmented by AI as a collaborative tool, to systematically address and resolve technical complexities.

By automating sentiment classification on Reddit data, Supersnu offers a scalable and robust solution for gaining deep insights into public opinion on any given topic.

## Recommendations

Potential future enhancements for Supersnu include:

-   Incorporating richer metadata (e.g., subreddit demographics, post flair, user history) to further contextualize sentiment.
-   Conducting A/B testing with different Gemini models or fine-tuning parameters like `temperature` to explore output variations.
-   Developing interactive visualization dashboards to dynamically present sentiment trends over time.
-   Extending data source support to other social media platforms for broader market analysis.
-   Implementing more granular error logging and monitoring features for production-grade deployments.

---

## How I Built Supersnu with AI Assistance (Focus on Gemini Implementation)

The development and refinement of the Gemini-based Supersnu was an advanced engineering endeavor, where AI assistance played a key role as a collaborative partner, particularly in navigating the intricacies of API migration and sophisticated debugging.

My collaboration with the AI involved:

-   **Strategic API Transition:** Transitioning the core sentiment analysis engine from an initial OpenRouter-based concept to the Google Gemini API. This involved a deep dive into updating API interaction patterns, authentication mechanisms, and response parsing strategies suitable for Gemini.
-   **Implementing Best-Practice Credential Security:** Engineering a secure system for handling API keys using environment variables (`os.environ.get()`), moving away from less secure practices. This included addressing and resolving shell-specific configuration details (like `zsh: bad assignment` nuances) and ensuring the Python script's architecture correctly interfaced with these environment variables.
-   **Systematic Resolution of Python Script Challenges:**
    *   Diagnosing and resolving file system path issues (`FileNotFoundError`) through standardized script execution protocols.
    *   Managing Python environment dependencies (`ModuleNotFoundError`) by ensuring correct installation of necessary packages (`google-generativeai`, `praw`) via `pip3`.
    *   Architecting global constants correctly within the Python script to prevent `NameError` issues related to environment variable name resolution.
-   **Optimizing Gemini API Interaction:** Designing the `call_gemini_api_batch` function for optimal performance and reliability. This included crafting effective prompts (`build_gemini_batch_prompt`) to elicit JSON-formatted responses, configuring `response_mime_type="application/json"`, and developing resilient parsing logic for Gemini's output, including handling potential markdown artifacts.
-   **Architecting for Script Robustness:** Implementing features like batch processing with clear progress indicators, comprehensive error logging, an intelligent retry mechanism for API calls, and a graceful fallback strategy for sentiment assignment in cases of unrecoverable API or parsing errors.
-   **Streamlining Data Output:** Enhancing the script to organize output CSVs into a dedicated `output_csvs` directory, improving project maintainability.

Throughout this process, the AI served as a valuable technical consultant, aiding in the analysis of error messages, suggesting optimized code structures for Python and terminal commands, and refining the logic for interacting with the Gemini API. This iterative, AI-augmented engineering approach was pivotal in developing a powerful and robust sentiment analysis tool.
