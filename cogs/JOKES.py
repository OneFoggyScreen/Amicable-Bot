#The cog all about memes and jokes

#--------- Libaries ---------#

import discord, asyncio, aiohttp, json, requests, sys
from discord.ext import commands
sys.path.append("../")
from tools.logging import ABLog
from tools.embeds import *

#--------- Code ---------#

class Jokes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='meme', aliases=['memes', 'me', 'Meme']) #Sends a meme on request
    async def image(self, context):
        async with aiohttp.ClientSession() as session:                               # Makes an aiohttp session and then sends a request to
            raw_response = await session.get("https://meme-api.herokuapp.com/gimme") # the meme API and then pulls the needed data.
            response = await raw_response.text()
            response = json.loads(response)
            ABLog("Meme Sent.")
            await context.send(embed=baseEmbed(response.get("title"), response.get("url")))



def setup(client):
	client.add_cog(Jokes(client))
