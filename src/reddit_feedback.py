import praw
import pandas as pd
from typing import List, Dict

def initialize_reddit(client_id: str, client_secret: str, user_agent: str) -> praw.Reddit:
    """Initialize and return a Reddit instance."""
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

def fetch_subreddit_posts(reddit: praw.Reddit, subreddit_name: str, limit: int = 500) -> List[Dict]:
    """Fetch posts from a subreddit and return as a list of dictionaries."""
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []

    for submission in subreddit.new(limit=limit):
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()[:3]
        top_comments = [comment.body[:400] for comment in comments]
        
        posts_data.append({
            "Title": submission.title,
            "URL": submission.url,
            "Description": submission.selftext[:800],
            "Top Comment 1": top_comments[0] if len(top_comments) > 0 else "",
            "Top Comment 2": top_comments[1] if len(top_comments) > 1 else "",
            "Top Comment 3": top_comments[2] if len(top_comments) > 2 else ""
        })

    return posts_data

def save_to_excel(data: List[Dict], filename: str):
    """Save the data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"Data written to {filename}")

if __name__ == "__main__":
    print("This script is not meant to be run directly. Please use main.py to execute the Reddit scraper.")