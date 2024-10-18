import asyncpraw
import asyncio

client_id = 'x'
client_secret = 'x'
user_agent = 'x x x'

async def fetch_reddit_stocks():
	reddit = asyncpraw.Reddit(
		client_id=client_id,
		client_secret=client_secret,
		user_agent=user_agent
		)
	subreddit = await reddit.subreddit("stocks")

	async for submission in subreddit.top(limit=10):

		print(f'{submission.title}')
		print(f'{submission.url}')

if __name__ == "__main__":
	asyncio.run(fetch_reddit_stocks())