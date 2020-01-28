import discord,os  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension,embedconfig

class log(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound):
            embed=discord.Embed(title=f"You type a wrong command!", color=embedconfig.embed_wrong)
        elif isinstance(error,commands.MissingPermissions):
            embed=discord.Embed(title="You don't have the permission to do that!", color=embedconfig.embed_wrong)
        elif isinstance(error,commands.MissingRequiredArgument):
            embed=discord.Embed(title="You need to specify a required argument!", color=embedconfig.embed_wrong)
        else:
            embed=discord.Embed(title=f"Unknown error,check the console log!", color=embedconfig.embed_wrong)
        embed.add_field(name="----------------------------", value=f"{error}", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(log(bot))    