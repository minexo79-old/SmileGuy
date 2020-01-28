import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

class embedconfig: # embed設定
    embed_pass = 0x80ff00
    embed_wrong = 0xff0000
    embed_normal = 0xffd300
    footer = 'SmileGuy Discord Bot'