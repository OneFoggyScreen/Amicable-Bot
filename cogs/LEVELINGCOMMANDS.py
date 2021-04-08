#Front end of leveling.

#--------- Libaries ---------#

import discord, json, sys
from discord.ext import commands
from collections import Counter
sys.path.append("../")
from tools.logging import ABLog
from tools.embeds import *
from settings import *

#--------- Code ---------#

class LevelCommands(commands.Cog):  #This is probably the stupidest code I've written which really says something about it.

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def leaderboard(self, ctx):
        with open('data/users.json', 'r') as f:
            users = json.load(f)
        leaders = {}
        for key in users[str(ctx.guild.id)].keys():
            leaders[str(key)] = users[str(ctx.guild.id)][str(key)]['exep'] 
        k = Counter(leaders)
        high = k.most_common(5)
        finals = ""
        for i in high:
            if str(i[0]) == BotsID: #--Might be-- Is Stupid.
                continue
            content = str(f'{ctx.bot.get_user(int(i[0]))} Has {i[1]}  Points \n')
            finals = finals + content
        await ctx.send(finals)

    @commands.command(aliases=["rank"])
    async def profile(self, ctx, *arg):
        with open('data/users.json', 'r') as f:
            users = json.load(f)
        if "@" in str(arg):
            user = str(list(arg))
            user = user.strip("<>@![]''")
        else:
            if str(arg) == "()":
                user = ctx.author.id
        try:
            level = users[str(ctx.guild.id)][str(user)]["level"]
            exe = users[str(ctx.guild.id)][str(user)]["exep"]
            ProfileEmbed = TwoFieldEmbed("Here's " + str(self.client.get_user(int(user)).name) + "'s Profile:", (str(self.client.get_user(int(user)).name) + "'s Experience:", str(exe)), (str(self.client.get_user(int(user)).name) + "'s Level:", str(level)), i1=True, i2=True)
            ProfileEmbed.set_thumbnail(url="https://cdn.discordapp.com/avatars/" + str(user) + "/" + str(self.client.get_user(int(user)).avatar) + ".png?size=1024")
            await ctx.send(embed=ProfileEmbed)
        except:
            await ctx.send("That person hasn't talked!")

def setup(client):
    client.add_cog(LevelCommands(client))

