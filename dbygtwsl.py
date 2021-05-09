import os
import sys
import discord
from discord_slash import SlashCommand

import discord.ext


"""
dbygtwsl version 2021.09.05
Developed by Anthony Provenza
Licensed under the MIT License
"""


bot = discord.ext.commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("Bot ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/dbygtwsl"))


@slash.slash(name="dbygtwsl",
             description="Send \"damn bro, you got the whole squad laughing\"")
async def dbygtwsl(ctx):
    f = discord.File(os.path.join(sys.path[0],
                                  "dbygtwsl.png"))
    await ctx.send(content="damn bro you got the whole squad laughing", file=f)


bot.run("")
