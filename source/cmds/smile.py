import discord # 導入discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import datetime
import json
import embedconfig
import pytz

tz = pytz.timezone('Asia/Taipei')

"""匯入設定檔json 建立jdata"""
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #互動設定檔
    jdata_bot = json.load(jfile_bot)
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #機器人設定檔
    jdata_bot = json.load(jfile_bot)

"""開機訊息"""
bot_m = '[Bot]'

"""顏色"""
blue_text = "in\033[34m"
white_text = "\033[0m"

class smile(Cog_Extension):
    """其他功能"""

    @commands.Cog.listener() #加入伺服器
    async def on_guild_join(self,guild):
        """時間設定"""
        time_stamp = datetime.datetime.now(tz).strftime('%Y.%m.%d-%H:%M:%S')
        embed=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=embedconfig.color)
        embed.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed.add_field(name="目前版本", value=jdata_bot['Version'], inline=True)
        embed.add_field(name="機器人作者", value="minexo79", inline=False)
        embed.add_field(name="指令幫助", value=jdata_bot['help'], inline=True)
        embed.set_footer(text=embedconfig.footer)
        channel = self.bot.get_channel(guild._system_channel_id) # 抓取預設聊天室ID
        print(bot_m,"joined at",guild.name,blue_text,time_stamp,white_text) #抓取伺服器名稱並且印在CLR上面
        await channel.send(embed=embed) #聊天室顯示加入訊息

    @commands.command() #ping查詢
    async def ping(self,ctx):
        embed = discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=embedconfig.color)
        embed.set_thumbnail(url="https://pic.sopili.net/pub/emoji/apple/64/1f9d0.png")
        embed.add_field(name="我目前的延遲", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)
    
    @commands.command() #關於
    async def about(self,ctx):
        embed1=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=embedconfig.color)
        embed1.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
        embed1.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed1.add_field(name="目前版本", value=jdata_bot['Version'], inline=True)
        embed1.add_field(name="機器人作者", value="minexo79", inline=False)
        embed1.add_field(name="指令幫助", value=jdata_bot['help'], inline=True)
        embed1.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed1) #聊天室顯示訊息
        embed2=discord.Embed(title="特別感謝",color=embedconfig.color)
        embed2.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed2.add_field(name="釣魚圖片繪製", value="```css\nSAIFRIX#1996\n```", inline=True)
        embed2.set_footer(text=embedconfig.footer)    
        await ctx.send(embed=embed2) #聊天室顯示訊息    
    
    @commands.command(pass_context = True) #HELP
    async def help(self,ctx):
        embed=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=embedconfig.color)
        embed.set_author(name="😀😀我可以用的功能😆😆")
        embed.set_thumbnail(url="https://pic.sopili.net/pub/emoji/apple/64/1f9d0.png")
        embed.add_field(name="關於", value="help `=>` 可用指令查詢\nabout `=>` 關於此機器人\ninfo `=>` 查詢伺服器狀態\nping `=>` 查詢延遲", inline=True)
        embed.add_field(name="釣魚(開發中)", value="fish now`=>` 開釣\nfish reg`=>` 玩家註冊\nfish exp`=>` 經驗查詢", inline=True)
        embed.add_field(name="其他", value="msgclear <數量> `=>` 清除訊息\nwea <英文地名> `=>` 天氣查詢\n訊息回復(Ex:蛤?)\n機器人加入通知", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed) #聊天室顯示訊息      

    @commands.command() #查詢伺服器狀態
    async def info(self,ctx):
        server_name = ctx.guild.name
        server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        server_user = len(ctx.guild.members)
        text_channel = len(ctx.guild.text_channels)
        voice_channel = len(ctx.guild.voice_channels)
        # embed 訊息
        embed = discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=embedconfig.color)
        embed.set_thumbnail(url="https://pic.sopili.net/pub/emoji/apple/64/1f9d0.png")
        embed.add_field(name="伺服器訊息", value=f"名稱：{server_name}\n創建日期：{server_create_date}\n伺服器人數：{server_user}\n文字頻道：{text_channel}\n語音頻道：{voice_channel}", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(smile(bot))  