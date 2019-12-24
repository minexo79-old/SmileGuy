import discord # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import time
import asyncio

"""匯入設定檔json 建立jdata"""
with open('setting_react.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)

class message(Cog_Extension):
    """訊息回復"""

    @commands.command() #清理訊息
    async def msgclear(self,ctx,num:int):
        await ctx.channel.purge(limit=num + 1)
        await ctx.send("訊息清除完畢!")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)   

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '蛤' and msg.author != self.bot.user: # 蛤
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG")
            embed.set_footer(text="https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG")
            await msg.channel.send(f"蛤?")            
            await msg.channel.send(embed=embed)

        elif msg.content == 'e04' and msg.author != self.bot.user: # 館長香蕉
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url="https://i.pinimg.com/originals/c9/75/65/c975658135e76db676aae7eca0ecc876.gif")
            embed.set_footer(text="https://i.pinimg.com/originals/c9/75/65/c975658135e76db676aae7eca0ecc876.gif")                
            await msg.channel.send(embed=embed)

        elif msg.content == '早' and msg.author != self.bot.user: # 早安
            ramdom_mes = random.choice(jdata_in[f'chat_mes_morning'])
            await msg.channel.send(f"{msg.author.mention} {ramdom_mes}")
            
        elif msg.content == '喔' and msg.author != self.bot.user: # 喔
            await msg.add_reaction("🤔")
            
        else:
            pass

def setup(bot):
    bot.add_cog(message(bot))  