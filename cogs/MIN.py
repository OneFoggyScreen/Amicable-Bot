#Help Command.

#--------- Libaries ---------#

import discord, sys
from discord.ext import commands
sys.path.append("../")
from settings import *
from tools.logging import ABLog
from tools.embeds import *

#--------- Code ---------#

class Helper(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def Help(self, context):
        await context.send(embed=TwoFieldEmbed("The help has arrived!", ("What's the prefix for this bot?", f"``{str(ABPrefixes)}``"), ("What commands does this bot have?", 
        "Currently we have ``blackjack``, ``meme``, ``music``, ``purge``, ``leaderboard``, ``profile``")))

    @commands.command(name='music', aliases=['Music', 'M'])
    async def MusicHelp(self, context):
        await context.send(embed=ThreeFieldEmbed("Music Commands", ("``connect``" , "Makes the bot join your voice channel"), 
        ("``play``", "Allows you to play a song. Accepts urls or names"), ("``disconnect / stop``", "Makes the bot leave the channel")))

def setup(client):
	client.add_cog(Helper(client))
