#Simple moderation

#--------- Libaries ---------#

import discord, sys
from discord.ext import commands
sys.path.append("../")
from tools.logging import ABLog

#--------- Code ---------#

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(name='Purge', aliases=['Clear', 'clear', 'purge']) #Simple purge command
	async def purge(self, context, args):
		if "bot" in [y.name.lower() for y in context.message.author.roles]: #Checks if user has premissions to do this and if not doesn't allow them.
			try:
				args = int(args)
				ABLog(f"Purged {str(args)} Messages") 
				await context.channel.purge(limit=args + 1)
			except:
				await context.send("Please use a number!")
		else:
			await context.send("You don't have the premissions to do this!")

def setup(client):
	client.add_cog(Moderation(client))
