#Makes embeds easy to use and with none of the clutter.

#--------- Libaries ---------#

import discord, sys
sys.path.append("../")
from settings import *

#--------- Code ---------#

def baseEmbed(Title, ImageURL, EmbedColor=Default_Color, FooterText=Name, FooterIconURL=BotImage): 
    """ A basic embed that has a name, profile picture, title, and image content """
    embedVar = discord.Embed(title=str(Title), color=EmbedColor)
    embedVar.set_image(url=str(ImageURL))
    embedVar.set_footer(text=FooterText, icon_url=FooterIconURL)
    return embedVar

def TwoFieldEmbed(Title, FieldOne, FieldTwo, EmbedColor=Default_Color, FooterText=Name, FooterIconURL=BotImage):
    """ A basic embed that has a name, title, and two fields for text 
        Takes Field values in a double, 0 being the name and 1 being the value. """
    embedVar = discord.Embed(title=str(Title), color=EmbedColor)
    embedVar.add_field(name=str(FieldOne[0]), value=str(FieldOne[1]), inline=False)
    embedVar.add_field(name=str(FieldTwo[0]), value=str(FieldTwo[1]), inline=False)
    embedVar.set_footer(text=FooterText, icon_url=FooterIconURL)
    return embedVar

def ThreeFieldEmbed(Title, FieldOne, FieldTwo, FieldThree, EmbedColor=Default_Color, FooterText=Name, FooterIconURL=BotImage):
    """ A basic embed that has a name, title, and three fields for text 
        Takes Field values in a double, 0 being the name and 1 being the value. """
    embedVar = discord.Embed(title=str(Title), color=EmbedColor)
    embedVar.add_field(name=str(FieldOne[0]), value=str(FieldOne[1]), inline=False)
    embedVar.add_field(name=str(FieldTwo[0]), value=str(FieldTwo[1]), inline=False)
    embedVar.add_field(name=str(FieldThree[0]), value=str(FieldThree[1]), inline=False)
    embedVar.set_footer(text=FooterText, icon_url=FooterIconURL)
    return embedVar