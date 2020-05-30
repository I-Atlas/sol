# Modules
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()  # load .env file
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
list_of_status = ['Hello there!', '🌌', 'Working on 2990WX', '☀', '🌻', '🚀']  # list of activities


# Task Loop
@tasks.loop(minutes=1)
async def change_presence():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.listening,
                                                        name=list_of_status[random.randint(0, 5)]))


# Bot Online Event
@bot.event
async def on_ready():
    print(f'{bot.user} is online!', '\nID:', bot.user.id, flush=True)
    change_presence.start()


# Load Cogs
if __name__ == '__main__':
    for cog_folder in os.listdir("cogs"):
        for cog in os.listdir(f"cogs/{cog_folder}"):
            if cog != "__pycache__":
                bot.load_extension(f"cogs.{cog_folder}.{cog[:-3]}")

# Load token from .env file
bot.run(os.getenv('TOKEN'))
