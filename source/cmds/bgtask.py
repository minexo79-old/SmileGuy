import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import os

"""開機訊息"""
bot_m = '[Bot]'

class bgtask(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        async def interval():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await self.bot.change_presence(status=discord.Status.online,activity=discord.Game("幫助：s!help")) #bot狀態
                await asyncio.sleep(10)
                await self.bot.change_presence(status=discord.Status.online,activity=discord.Game("SmileGuys Running!")) #bot狀態
                await asyncio.sleep(10)                     

        self.bg_task = self.bot.loop.create_task(interval())
            
def setup(bot):
    bot.add_cog(bgtask(bot))