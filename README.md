![lilmunkeycirc](https://github.com/user-attachments/assets/3a7c7e0e-9501-4ad2-aaeb-64686ce20dd5)

# Reddit Discord
A bot using discord.py and asyncpraw to return 10 results from any subreddit.  
- $posts cars top 2 - this command will return the top 2 results for the subreddit news
![image](https://github.com/user-attachments/assets/5f50ad2c-a133-41d3-a7cd-cff57b2db32e)
  

- $google cars - this will return any results found using degoogle
![image](https://github.com/user-attachments/assets/3f116d24-2845-4c80-a9b4-0626b1d27fe1)


## To Do
- Commands:
  +    (Current) Usage: $posts [(subreddit)] [new/top] [Number of Posts]      
  +    Add more features with [commands](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html).
- Messages - Return each post link instead of a list, format each response, create more detailed views.
- Content - Use more APIs to gather interesting data to post to discord (eg. Financial news, security news,weather reports, youtube)
- Degoogle - optimize and make search results more robust and relevant
- Fix install script for degoogle git repository and automatic virtulenv setup

# Developer Links 
- https://developers.reddit.com/
- https://discord.com/developers/applications

# Install Instructions
- git clone
- cd reddit-discord/bot
- python -m pip install -r requirememnts.txt
- python -m virtualenv venv
- ./venv/scripts/activate or source ./venv/bin/activate (depending on MS or Linux)
- python bot.py
