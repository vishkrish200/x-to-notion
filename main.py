import os
import asyncio
from dotenv import load_dotenv
import twikit
import requests

USERNAME = 'slimylemon'
EMAIL = 'vishkrish200@gmail.com'
PASSWORD = ''

# Load environment variables
load_dotenv()

# Twitter API credentials
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Notion API credentials
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def get_twitter_client():
    return twikit.Client(
        bearer_token=TWITTER_BEARER_TOKEN,
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_SECRET
    )

def get_bookmarks(client):
    # Fetch bookmarks using twikit
    # This is a placeholder and needs to be implemented based on twikit's API
    pass

def add_to_notion(bookmarks):
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    for bookmark in bookmarks:
        data = {
            "parent": {"database_id": NOTION_DATABASE_ID},
            "properties": {
                "Title": {"title": [{"text": {"content": bookmark['text']}}]},
                "URL": {"url": bookmark['url']}
            }
        }
        
        response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)
        if response.status_code != 200:
            print(f"Failed to add bookmark: {response.text}")

def main():
    twitter_client = get_twitter_client()
    bookmarks = get_bookmarks(twitter_client)
    add_to_notion(bookmarks)

if __name__ == "__main__":
    main()

