import discord,os  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension

class log(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound):
            await ctx.send(f"You type a wrong command: **{ctx.message.content}**.")
        if isinstance(error,commands.CheckFailure):
            await ctx.send(f"You don't have the permission to do that!")
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(f"You need to specify a required argument.") 

def setup(bot):
    bot.add_cog(log(bot))    