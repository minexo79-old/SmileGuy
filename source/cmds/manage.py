import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio

"""匯入設定檔json 建立jdata"""
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #互動設定檔
    jdata_bot = json.load(jfile_bot)

bot_m = '[Bot]'

class reloadcog(Cog_Extension):
    """模組重裝"""

    @commands.command() #清理訊息
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num + 1)
        await ctx.send("訊息清除完畢!")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)  
        pass 

    @commands.command()
    async def load(self,ctx,extension): #載入模組
        if ctx.author.id == int(jdata_bot['Owner']):
            await ctx.channel.purge(limit=1)
            self.bot.load_extension(f'cmds.{extension}')
            print(bot_m,f"<{extension}> load complete.")
            await ctx.send(f">>> 模組 {extension} 已載入。")
        else:
            pass

    @commands.command()
    async def unload(self,ctx,extension): #卸載模組
        if ctx.author.id == int(jdata_bot['Owner']):
            await ctx.channel.purge(limit=1)
            self.bot.unload_extension(f'cmds.{extension}')
            print(bot_m,f"<{extension}> unload complete.")
            await ctx.send(f">>> 模組 {extension} 已卸載。")
        else:
            pass

    @commands.command()
    async def reload(self,ctx,extension): #重裝模組
        if ctx.author.id == int(jdata_bot['Owner']):
            await ctx.channel.purge(limit=1)
            self.bot.reload_extension(f'cmds.{extension}')
            print(bot_m,f"<{extension}> reload complete.")
            await ctx.send(f">>> 模組 {extension} 已重裝。")
        else:
            pass

def setup(bot):
    bot.add_cog(reloadcog(bot))  