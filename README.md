# Feedback Analyzer

This repository contains scripts to collect and analyze customer feedback for specific products from Reddit and the App Store. It helps in identifying key customer pain points and generating insights from user reviews.

## Features

- Collect recent posts and comments from a specified subreddit
- Scrape reviews from the Apple App Store for a given app
- Generate histograms of App Store review summaries
- Generate histograms of Reddit feedback
- Export collected data to Excel files for further analysis

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/FeedbackAnalyzer.git
   cd FeedbackAnalyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Reddit API credentials:
   - Create a Reddit account and navigate to https://www.reddit.com/prefs/apps
   - Create a new app, select "script" as the type
   - Note down the client ID and client secret

4. Set up environment variables:
   - Create a `.env` file in the root directory with the following content:
     ```
     REDDIT_CLIENT_ID=your_client_id
     REDDIT_CLIENT_SECRET=your_client_secret
     REDDIT_USER_AGENT=your_user_agent
     ```
   - Replace `your_client_id`, `your_client_secret`, and `your_user_agent` with your actual Reddit API credentials.

## Usage

To run the entire data collection and analysis process, use the following command:

```
python -m src.main
```

This will:
1. Collect feedback from the specified subreddit
2. Scrape reviews from the App Store
3. Generate a histogram of App Store review summaries
4. Generate a histogram of Reddit feedback

The results will be saved as Excel files (`reddit_AVP_feedback.xlsx` and `applesupport_app_reviews.xlsx`) and SVG files (`review_summaries_histogram.svg` and `avp_reddit_histogram_dark_transparent.svg`) in the project directory.

## Customization

You can customize the subreddit, app, and other parameters by modifying the `src/main.py` file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.