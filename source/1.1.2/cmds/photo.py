import discord # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

"""#匯入設定檔json 建立jdata"""
with open('setting_react.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)
with open('setting_chatphoto.json',mode='r',encoding='utf8') as jfile_chatphoto: #機器人訊息
    jdata_chatphoto = json.load(jfile_chatphoto)

"""開機訊息"""
bot_m = '[Bot]'

class photo(Cog_Extension):
    """梗圖功能"""

    @commands.command() #發梗圖
    async def photo(self,ctx):
        random_pic = random.choice(jdata_chatphoto['chat_photo']) #隨機選取網址
        ramdom_mes = random.choice(jdata_in['chat_photo_mes']) #隨機選取訊息
        embed = discord.Embed(color=0xffd300)
        embed.set_author(name=ramdom_mes)
        embed.set_image(url=random_pic)
        await ctx.send(embed=embed)

    @commands.command() #加梗圖
    async def addphoto(self,ctx,msg):
        wr = jdata_chatphoto['chat_photo'] #指定元素
        wr.append(msg) #增加網址
        with open('setting_chatphoto.json',mode='w',encoding='utf8') as jsave: #權限改成寫入
            data = {
                "chat_photo":wr #格式
            }
            json.dump(data,jsave,indent=2) #存檔
            embed = discord.Embed(color=0xffd300)
            embed.add_field(name="訊息", value=jdata_in['chat_photo_add'], inline=False)
            embed.set_footer(text="SmileGuy Discord Bot")
            await ctx.send(embed=embed) #聊天室

    @commands.command() #刪梗圖
    async def delphoto(self,ctx,msg):
        wr = jdata_chatphoto['chat_photo'] #指定元素
        wr.remove(msg) #刪除網址
        with open('setting_chatphoto.json',mode='w',encoding='utf8') as jsave: #權限改成寫入
            data = {
                "chat_photo":wr #格式
            }
            json.dump(data,jsave,indent=2) #存檔
            embed = discord.Embed(color=0xffd300)
            embed.add_field(name="訊息", value=jdata_in['chat_photo_del'], inline=False)
            embed.set_footer(text="SmileGuy Discord Bot")
            await ctx.send(embed=embed) #聊天室

    @commands.command() #梗圖查詢
    async def photolist(self,ctx):
        photo = 0
        for wr in jdata_chatphoto['chat_photo']:
            wr_L = f'```http\n{wr}\n```'
            await ctx.send(wr_L)
            photo = photo + 1
        embed = discord.Embed(color=0xffd300)
        embed.add_field(name="查詢結果", value=f"共有{photo}張圖片!", inline=False)
        embed.set_footer(text="SmileGuy Discord Bot")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(photo(bot))     