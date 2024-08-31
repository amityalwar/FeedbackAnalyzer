import os
import praw
from .reddit_feedback import initialize_reddit, fetch_subreddit_posts, save_to_excel as save_reddit_data
from .appstore_feedback import fetch_app_reviews, save_to_excel as save_appstore_data
from .plot_histogram_app_reviews import generate_histogram as generate_appstore_histogram
from .plot_histogram_reddit import generate_reddit_histogram

def run_reddit_scraper():
    print("Starting Reddit scraper...")
    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
    user_agent = os.environ.get('REDDIT_USER_AGENT', 'my_reddit_feedback_app')

    if not all([client_id, client_secret]):
        raise ValueError("Reddit API credentials not found in environment variables.")

    reddit = initialize_reddit(client_id, client_secret, user_agent)
    subreddit_name = 'VisionPro'
    posts_data = fetch_subreddit_posts(reddit, subreddit_name)
    save_reddit_data(posts_data, 'reddit_AVP_feedback.xlsx')
    print("Reddit scraping completed.")

def run_appstore_scraper():
    print("Starting App Store scraper...")
    app_name = "apple-support"
    app_id = "1130498044"
    country = "us"
    reviews = fetch_app_reviews(country, app_name, app_id)
    save_appstore_data(reviews, "applesupport_app_reviews.xlsx")
    print("App Store scraping completed.")

def run_appstore_histogram_generation():
    print("Generating App Store histogram...")
    input_file = 'applesupport_app_reviews.xlsx'
    output_file = 'review_summaries_histogram.svg'
    generate_appstore_histogram(input_file, output_file)
    print(f"App Store histogram generated and saved as {output_file}")

def run_reddit_histogram_generation():
    print("Generating Reddit histogram...")
    input_file = 'reddit_AVP_feedback.xlsx'
    output_file = 'avp_reddit_histogram_dark_transparent.svg'
    generate_reddit_histogram(input_file, output_file)
    print(f"Reddit histogram generated and saved as {output_file}")

def main():
    print("Starting Product Feedback Analyzer...")
    
    run_reddit_scraper()
    run_appstore_scraper()
    run_appstore_histogram_generation()
    run_reddit_histogram_generation()
    
    print("All tasks completed successfully.")

if __name__ == "__main__":
    main()