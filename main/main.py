import discord
from discord.ext import commands
from discord.flags import Intents
import music

cogs = [music]
client = commands.Bot(command_prefix=".", intents= discord.Intents.all())
for i in range(len(cogs)):
    cogs[i].setup(client)
client.run("OTI4MDYxMjU1NTY5MjYwNTU1.YdTSZQ.-oBSh3agpOiftSBQHJwijvLG6ZU")