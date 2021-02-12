#Simple role assigner 

#--------- Libaries ---------#

import discord, json, sys
from discord.ext import commands
sys.path.append("../")
from tools.logging import ABLog

#--------- Code ---------#

class Welcomer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #Adds the role to the reactor.
    async def on_raw_reaction_add(self, payload):
        with open('data/messageid.json', 'r') as f: #Checks if the message is marked
            MESID = json.load(f)
        message_id = payload.message_id
        if str(message_id) in MESID: #If in, then add.
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None: #Error checking.
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                else:
                    ABLog("No Member")
            else:
                ABLog("Role Not found")

    @commands.Cog.listener() #Removes the role from the reactor.
    async def on_raw_reaction_remove(self, payload):
        with open('data/messageid.json', 'r') as f: #Checks if the message is marked
            MESID = json.load(f)
        message_id = payload.message_id
        if str(message_id) in MESID: #If in, then add.
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None: #Error checking.
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                else:
                    ABLog("No Member")
            else:
                ABLog("Role Not found")

    @commands.command() #Adds a message to the marked list.
    async def mark(self, ctx, arg):
        if "bot" in [y.name.lower() for y in ctx.message.author.roles]:
            with open('data/messageid.json', 'r') as f: #Checks list.
                MESID = json.load(f)
            if not str(arg) in MESID: #Makes sure not already in list.
                MESID[str(arg)] = {}
            else:
                pass
            with open('data/messageid.json', 'w') as f: #Writes to the list
                json.dump(MESID, f)
            await ctx.send("Messaged marked!", delete_after=5)
        else:
            await ctx.send("You don't have premission to do that!")


def setup(client):
	client.add_cog(Welcomer(client))
