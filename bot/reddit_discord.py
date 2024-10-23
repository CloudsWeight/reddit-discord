import asyncpraw
import asyncio
import os 
import dotenv
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('SECRET')
user_agent = os.getenv('USER')

async def fetch_reddit_stocks(subreddit, cat='new', amount=10 ):
	N = amount
	reddit = asyncpraw.Reddit(
		client_id=client_id,
		client_secret=client_secret,
		user_agent=user_agent
		)
	subreddit = await reddit.subreddit(subreddit)
	posts = []
	if cat == 'new':
		async for submission in subreddit.new(limit=N):
			post_info = {"title": submission.title, "url": submission.url}
			posts.append(post_info)
	elif cat == 'top':
		async for submission in subreddit.top(limit=N):
			post_info = {"title": submission.title, "url": submission.url}
			posts.append(post_info)
	else:
		async for submission in subreddit.new(limit=N):
			post_info = {"title": submission.title, "url": submission.url}
			posts.append(post_info)

	return posts
	
if __name__ == "__main__":
	asyncio.run(fetch_reddit_stocks())
