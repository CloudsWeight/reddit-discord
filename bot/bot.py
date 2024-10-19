import discord
from dotenv import load_dotenv
import os
from gensamford import fetch_reddit_stocks
import asyncio
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class GenSam(discord.Client):
	#posts = asyncio.run(fetch_reddit_stocks()) pre-fetching?
	async def on_ready(self):
		print(f'bot ready {self.user}')

	async def on_message(self, message):
		if message.author == self.user:
			return 
		if message.content == 'ping':
			await message.channel.send('pong')
		if message.content == "posts":
			await message.channel.send(self.posts)

intents = discord.Intents.default()
intents.message_content = True 
client = GenSam(intents=intents)
client.run(TOKEN)
