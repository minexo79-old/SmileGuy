import discord # 導入discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import requests #抓取HTTP網頁資訊
import json

class weather(Cog_Extension):
    """天氣查詢"""

    @commands.command() #天氣
    async def wea(self,ctx):
        cityname = ctx.channel.last_message.content
        city = cityname.lstrip('!wea ') #去除指令
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=be8b9dcc6ba7e9892115c583aec589ed&units=metric'.format(city)
        data = requests.get(url).json()
        code = data['cod']
        if code == '404': # 城市輸入錯誤
            embed=discord.Embed(color=0xffd300)
            embed.add_field(name="🌏錯誤!!", value="**找不到天氣資訊**", inline=False)
            embed.set_footer(text="SmileGuy Discord Bot")
            await ctx.send(embed=embed)
        elif code != '404': # 城市輸入正確
            # 抓取資訊
            max_temp = data['main']['temp_max'] #高溫
            min_temp = data['main']['temp_min'] #低溫
            humidity = data['main']['humidity'] #濕度
            temp = data['main']['temp'] #溫度
            city = data['name'] #城市
            overview = data['weather'][0]['main'] #概況
            country = data['sys']['country'] #國家
            icon = data['weather'][0]['icon']
            # embed
            embed=discord.Embed(title=f"🌏天氣資訊",description="資料來源:openweathermap.org",url="https://openweathermap.org/",color=0xffd300)
            embed.set_thumbnail(url=f"https://openweathermap.org/img/w/{icon}.png") #天氣圖標
            embed.add_field(name="目前溫度(範圍)", value=f'{temp}℃({min_temp}~{max_temp})', inline=False)  
            embed.add_field(name="天氣概況", value=f'{overview}', inline=False)        
            embed.add_field(name="濕度", value=f'{humidity}%', inline=True)
            embed.add_field(name="城市", value=f'{city}/{country}', inline=True)
            embed.set_footer(text="SmileGuy Discord Bot")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(weather(bot))