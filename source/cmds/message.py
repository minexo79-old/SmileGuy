import discord # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension,embedconfig
import random
import json

with open('setting_react.json',mode='r',encoding='utf8') as jfile_react: #互動設定檔
    jdata_react = json.load(jfile_react)

class message(Cog_Extension):
    """訊息回復""" 

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '蛤' and msg.author != self.bot.user: # 蛤
            embed = discord.Embed(color=embedconfig.embed_normal)
            embed.set_image(url="https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG")
            embed.set_footer(text="https://truth.bahamut.com.tw/s01/201809/19336b6cfc3198bd9c7e9bf564eb1223.JPG")
            await msg.channel.send(f"蛤?")            
            await msg.channel.send(embed=embed)

        elif msg.content == 'e04' and msg.author != self.bot.user: # 館長香蕉
            embed = discord.Embed(color=embedconfig.embed_normal)
            embed.set_image(url="https://i.pinimg.com/originals/c9/75/65/c975658135e76db676aae7eca0ecc876.gif")
            embed.set_footer(text="https://i.pinimg.com/originals/c9/75/65/c975658135e76db676aae7eca0ecc876.gif")                
            await msg.channel.send(embed=embed)

        elif msg.content in jdata_react[f'morning_prefix'] and msg.author != self.bot.user: # 早安
            ramdom_mes = random.choice(jdata_react[f'morning_react'])
            await msg.channel.send(f"{msg.author.mention} {ramdom_mes}")
        
        elif msg.content == "火焰!" and msg.author != self.bot.user:
            embed = discord.Embed(color=embedconfig.embed_normal)
            embed.set_image(url="https://i.imgur.com/z8Hhhoz.jpg")
            embed.set_footer(text="https://i.imgur.com/z8Hhhoz.jpg")
            await msg.channel.send(embed=embed)            

        elif msg.content == '喔' and msg.author != self.bot.user: # 喔
            await msg.add_reaction("🤔")
            
        else:
            pass

def setup(bot):
    bot.add_cog(message(bot))  