import asyncpraw
import asyncio
import os 
import dotenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('SECRET')
user_agent = os.getenv('USER')

async def fetch_reddit_stocks():
	reddit = asyncpraw.Reddit(
		client_id=client_id,
		client_secret=client_secret,
		user_agent=user_agent
		)
	subreddit = await reddit.subreddit("stocks")
	posts = []
	async for submission in subreddit.new(limit=10):
		post_info = f'{submission.title}\n{submission.url}'
		posts.append(post_info)
		#print(post_info)
	return posts

class GenSamford(discord.Client):
	async def on_ready(self):
		channel = self.get_channel('')

		if channel is not None:
			posts = await fetch_reddit_stocks()
			for post in posts:
				await channel.send(post)

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = GenSamford(intents=intents)

#async def main():
	

if __name__ == "__main__":
	asyncio.run(fetch_reddit_stocks())
	

