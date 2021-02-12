#The heart of the bot.

#--------- Libaries ---------#

import discord, os, settings
from tools.logging import ABLog
from discord.ext import commands

#--------- Variables ---------#

INTENTS = discord.Intents.all()
client = commands.Bot(command_prefix = settings.ABPrefixes, intents = INTENTS, help_command=None)
client.remove_command('help')

#--------- Code ---------#


@client.command() #Loads specified cog.
async def load(ctx, extension): 
	if ctx.message.author.id == settings.AdminID:
		client.load_extension(f'cogs.{extension}')
		ABLog(f"Loading {extension}")
		await ctx.send(f'The cog {extension} was loaded')


@client.command() #Reloads specified cog.
async def reload(ctx, extension):
	if ctx.message.author.id == settings.AdminID:
		client.reload_extension(f'cogs.{extension}')
		ABLog(f"Reloading {extension}")
		await ctx.send(f'The cog {extension} was reloaded')


@client.command() #Unloads specified cog.
async def unload(ctx, extension):
	if ctx.message.author.id == settings.AdminID:
		client.unload_extension(f'cogs.{extension}')
		ABLog(f"Unloading {extension}")
		await ctx.send(f'The cog {extension} was unloaded')


for filename in os.listdir('./cogs'): #Initial load of all cogs.
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f"Loaded {filename}")


@client.event #Changes the custom status.
async def on_ready():
    activity = discord.Activity(name=settings.Custom_Status, type=discord.ActivityType.playing)
    ABLog("Bot loaded.")
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=activity)


client.run(settings.Token) #Gets the bot online!
