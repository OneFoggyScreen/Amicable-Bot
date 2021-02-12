#Simple money system. 

#--------- Libaries ---------#

import discord, json, sys
from discord.ext import commands
sys.path.append("../")
from tools.logging import ABLog

#--------- Code ---------#

class EconBackEnd(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('data/econ.json', 'r') as f:
            users = json.load(f)
        await update_data(users, message.author)
        with open('data/econ.json', 'w') as f:
            json.dump(users, f)

def setup(client):
	client.add_cog(EconBackEnd(client))

async def update_data(users, user):
    userstring = str(user.id)
    if not userstring in users:
        users[userstring] = {}
        users[userstring]['coins'] = 5


