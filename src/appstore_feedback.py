from app_store_scraper import AppStore
import pandas as pd
from typing import List, Dict

def fetch_app_reviews(country: str, app_name: str, app_id: str, limit: int = 1000) -> List[Dict]:
    """Fetch reviews for an app from the App Store."""
    app_scraper = AppStore(country=country, app_name=app_name, app_id=app_id)
    app_scraper.review(how_many=limit)

    reviews_data = [{
        "Date": review['date'],
        "Rating": review['rating'],
        "Review": review['review'],
    } for review in app_scraper.reviews]

    return reviews_data

def save_to_excel(data: List[Dict], filename: str):
    """Save the data to an Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"Data written to {filename}")

if __name__ == "__main__":
    print("This script is not meant to be run directly. Please use main.py to execute the App Store scraper.")  