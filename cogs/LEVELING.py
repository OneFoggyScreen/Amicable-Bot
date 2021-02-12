#Back end for leveling.

#--------- Libaries ---------#

import discord, json, sys
from discord.ext import commands
sys.path.append("../")
from tools.logging import ABLog
from tools.embeds import *
from settings import *

#--------- Code ---------#

class LevelingLogic(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        with open('data/users.json', 'r') as f:
            users = json.load(f)

        guild = message.author.guild

        await update_data(users, message.author, guild)
        await add_exep(users, message.author, guild)
        await leaderboard_update(users, message.author, guild, message)

        with open('data/users.json', 'w') as f:
            json.dump(users, f)

    async def on_member_join(self, member):
        with open('data/users.json', 'r') as f:
            users = json.load(f)

        guild = member.guild
        await update_data(users, member, guild)

        with open('data/users.json', 'w') as f:
            json.dump(users, f)

def setup(client):
	client.add_cog(LevelingLogic(client))

#--------- Functions ---------#

async def update_data(users, user, guild):
    userstring = str(user.id)
    if not str(guild.id) in users:
        users[str(guild.id)] = {}
        users[str(guild.id)][userstring] = {}
        users[str(guild.id)][userstring]['exep'] = 0
        users[str(guild.id)][userstring]['level'] = 1
    else:
        if not userstring in users[str(guild.id)]:
            users[str(guild.id)][userstring] = {}
            users[str(guild.id)][userstring]['exep'] = 0
            users[str(guild.id)][userstring]['level'] = 1


async def add_exep(users, user, guild):
    users[str(guild.id)][str(user.id)]['exep'] += 5

async def leaderboard_update(users, user, guild, message):
    userstring = str(user.id)
    exp = users[str(guild.id)][userstring]['exep']
    lvl_stat = users[str(guild.id)][userstring]['level']
    lvl_end = int(exp ** (1/4))

    if lvl_stat < lvl_end:
        if not str(message.author.id) == BotsID:
            await message.channel.send(f'{message.author.mention} has leveled up to Level ' + str(lvl_end) + '. Congrats!')
            users[str(guild.id)][userstring]['level'] = lvl_end
