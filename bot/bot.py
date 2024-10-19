import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from gensamford import fetch_reddit_stocks
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class GenSam(commands.Bot):
    def __init__(self, command_prefix, intents):
        commands.Bot.__init__(self, command_prefix=command_prefix, intents=intents)
        self.add_commands()
        
    
    async def on_ready(self):
        print(f'Bot ready')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message) 

    def add_commands(self):
        @self.command(name="ping", pass_context=True)
        async def ping(ctx):
            await ctx.send("pong")
        
        @self.command(name="posts", pass_context=True)
        async def posts(ctx, subreddit):
            posts = await fetch_reddit_stocks(subreddit)
            await ctx.send(posts)
        


intents = discord.Intents.default()
intents.message_content = True

client = GenSam(command_prefix="$", intents=intents)

client.run(TOKEN)