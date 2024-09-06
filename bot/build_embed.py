import discord
import datetime
from discord import Guild


async def build(title, description, color):
    embed = discord.Embed(
        title=f"{title}",
        description=f"{description}",
        color=color
        )
    # embed.set_footer(text='SB Shop Bot', icon_url='https://cdn.discordapp.com/avatars/1276317106819825746/01a3154bc42012e945828e266c7ace51.webp?size=80')
    # embed.timestamp = datetime.datetime.now()
    return embed
