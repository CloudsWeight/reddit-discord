import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from reddit_discord import fetch_reddit_stocks
import asyncio
import subprocess
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class GenSam(commands.Bot):
    
    def __init__(self, command_prefix='$', intents=None):
        commands.Bot.__init__(self, command_prefix=command_prefix, intents=intents)
        self.add_commands()
    
    async def on_ready(self):
        print(f'Bot ready')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message) 

    def add_commands(self):
        try:

            @self.command(name="ping", pass_context=True)
            async def ping(ctx):
                await ctx.send("pong")

            @self.command(name="posts", pass_context=True)
            async def posts(ctx, subreddit, cat='new', amount=10 ): 
                posts = await fetch_reddit_stocks(subreddit, cat, amount)
                embed_posts = discord.Embed(title=f"Displaying {amount} {cat.title()} Posts from r/{subreddit}", description=f"Put Subreddit description here", color=0xFF5700)
                for i, post in enumerate(posts):
                    embed_posts.add_field(name=f"#{i + 1}) {post['title']}", value=f"[{post['title']}]({post['url']})", inline=False)
                await ctx.send(embed=embed_posts)
                
            @self.command(name="google", pass_context=True)
            async def google(ctx, search='developing'): 
                raw_posts = subprocess.check_output(f'degoogle {search}')
                posts = raw_posts.decode('ascii')
                embed_posts = discord.Embed(title=f"Search Results for: {search}", description=f"Put Subreddit description here", color=0xFF5700)
                i = 0
                if posts != None:
                    embed_posts.add_field(name=f"#{i + 1})", value=posts,  inline=False)
                await ctx.send(embed=embed_posts)
        except Exception as e:
            print(f'ERROR ENCOUNTERED see below:\n{e}')

intents = discord.Intents.default()
intents.message_content = True
client = GenSam(command_prefix='$', intents=intents)
client.run(TOKEN)
