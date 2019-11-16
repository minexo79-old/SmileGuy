import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

class bgtask(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        async def interval():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                self.bot.reload_extension(f'cmds.fishing')
                await asyncio.sleep(60)

        self.bg_task = self.bot.loop.create_task(interval())
            
def setup(bot):
    bot.add_cog(bgtask(bot))