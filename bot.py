import discord
from discord.ext import commands
import os
import config

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online.")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("---------------------------------------")
        print(f"Loaded Cog:\n{filename[:-3]}")
        print("---------------------------------------")
    else:
        continue

bot.login(config.token)