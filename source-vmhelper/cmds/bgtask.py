import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import os

bot_m = "[VM]"

class bgtask(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        async def interval(): #每60秒重裝一次模組
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                for filename in os.listdir('./cmds'):
                    if filename.endswith('.py'):
                        self.bot.reload_extension('cmds.fishing')
                        print(bot_m,"Auto reload.")
                        await asyncio.sleep(100)

        self.bg_task = self.bot.loop.create_task(interval())
            
def setup(bot):
    bot.add_cog(bgtask(bot))