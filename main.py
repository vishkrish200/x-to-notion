import os
import asyncio
from dotenv import load_dotenv
import tweepy
import requests
import webbrowser

# Load environment variables
load_dotenv()

# Twitter API Credentials
CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")
REDIRECT_URI = os.getenv("TWITTER_REDIRECT_URI")

# Notion API credentials
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

async def get_twitter_client():
    oauth2_user_handler = tweepy.OAuth2UserHandler(
        client_id=CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=["tweet.read", "users.read", "bookmark.read"],
        client_secret=CLIENT_SECRET
    )

    print(f"Please go to this URL and authorize the app: {oauth2_user_handler.get_authorization_url()}")
    webbrowser.open(oauth2_user_handler.get_authorization_url())
    
    callback_url = input("Paste the callback URL here: ")
    access_token = oauth2_user_handler.fetch_token(callback_url)

    return tweepy.Client(access_token)

async def get_bookmarks(client):
    bookmarks = client.get_bookmarks(expansions=['author_id'], tweet_fields=['created_at'])
    return bookmarks.data, bookmarks.includes['users']

async def add_to_notion(bookmarks, users):
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    user_dict = {user.id: user for user in users}
    
    for bookmark in bookmarks:
        author = user_dict.get(bookmark.author_id)
        data = {
            "parent": {"database_id": NOTION_DATABASE_ID},
            "properties": {
                "Title": {"title": [{"text": {"content": bookmark.text[:100]}}]},
                "URL": {"url": f"https://twitter.com/i/web/status/{bookmark.id}"},
                "Author": {"rich_text": [{"text": {"content": author.name if author else "Unknown"}}]},
                "Created At": {"date": {"start": bookmark.created_at.isoformat()}}
            }
        }
        
        response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)
        if response.status_code != 200:
            print(f"Failed to add bookmark: {response.text}")
        else:
            print(f"Successfully added bookmark: {bookmark.text[:50]}...")

async def main():
    try:
        client = await get_twitter_client()
        bookmarks, users = await get_bookmarks(client)
        print(f"Retrieved {len(bookmarks)} bookmarks")

        await add_to_notion(bookmarks, users)
        print("Finished adding bookmarks to Notion")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
