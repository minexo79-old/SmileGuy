import discord # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

"""#匯入設定檔json 建立jdata"""
with open('setting_react.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)

class message(Cog_Extension):
    """回應功能"""

    @commands.Cog.listener() #三修
    async def on_message(self,msg):
        keyword = ['三修','三小','WTF','蛤']
        if msg.content in keyword and msg.author != self.bot.user:
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url='https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG')
            await msg.channel.send('蛤?')
            await msg.channel.send(embed=embed)

    @commands.Cog.listener() #加油
    async def on_message(self,msg):
        keyword = ['加油','加油阿','加油!']
        if msg.content in keyword and msg.author != self.bot.user:
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url='https://www.jiuwa.net/tuku/20180103/uNzVOquq.jpg')
            await msg.channel.send('加油喔!')
            await msg.channel.send(embed=embed)
    
    @commands.Cog.listener() #我們懷念他
    async def on_message(self,msg):
        keyword = ['懷念','\|/','懷念他','懷念你','我們懷念他']
        if msg.content in keyword and msg.author != self.bot.user:
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url='http://i.imgur.com/In1clUx.jpg')
            await msg.channel.send('我們懷念他')
            await msg.channel.send(embed=embed)

    @commands.Cog.listener() #氣氣氣氣氣
    async def on_message(self,msg):
        keyword = ['氣','氣氣氣','氣氣氣氣氣','喔氣氣氣氣氣']        
        if msg.content in keyword and msg.author != self.bot.user:
            embed = discord.Embed(color=0xffd300)
            embed.set_image(url='https://i.ytimg.com/vi/mYQppvw4HGY/maxresdefault.jpg')
            await msg.channel.send('喔 氣氣氣氣氣~~~')
            await msg.channel.send(embed=embed)        

def setup(bot):
    bot.add_cog(message(bot))   