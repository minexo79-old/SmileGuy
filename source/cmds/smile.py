import discord # 導入discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension,embedconfig
import datetime
import json
import pytz

tz = pytz.timezone('Asia/Taipei')

"""匯入設定檔json 建立jdata"""
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #互動設定檔
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
        time_stamp = datetime.datetime.now(tz).strftime('%Y.%m.%d-%H:%M:%S')
        embed=discord.Embed(title="我的原始碼", url="https://github.com/minexo79/SmileGuy",color=embedconfig.embed_normal)
        embed.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed.set_footer(text=embedconfig.footer)
        channel = self.bot.get_channel(guild._system_channel_id) # 抓取預設聊天室ID
        print(bot_m + "joined at" + guild.name + blue_text + time_stamp + white_text) #抓取伺服器名稱並且印在CLR上面
        await channel.send(embed=embed) #聊天室顯示加入訊息

    @commands.command() #ping查詢
    async def ping(self,ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="我的原始碼", url="https://github.com/minexo79/SmileGuy",color=embedconfig.embed_normal)
        embed.set_thumbnail(url="https://pic.sopili.net/pub/emoji/apple/64/1f9d0.png")
        embed.add_field(name="Ping", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)
    
    @commands.command() #關於
    async def about(self,ctx):
        await ctx.channel.purge(limit=1)
        embed1=discord.Embed(title="我的原始碼", url="https://github.com/minexo79/SmileGuy",color=embedconfig.embed_normal)
        embed1.set_author(name="😀😀關於😆😆")
        embed1.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
        embed1.add_field(name="目前版本", value=jdata_bot['Version'], inline=False)
        embed1.add_field(name="機器人作者", value="minexo79", inline=False)
        embed1.add_field(name="指令幫助", value=jdata_bot['help'], inline=False)
        embed1.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed1) #聊天室顯示訊息  
    
    @commands.command(pass_context = True) #HELP
    async def help(self,ctx):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="我的原始碼", url="https://github.com/minexo79/SmileGuy",color=embedconfig.embed_normal)
        embed.set_author(name="😀😀機器人指令😆😆")
        embed.set_thumbnail(url="https://pic.sopili.net/pub/emoji/apple/64/1f9d0.png")
        embed.add_field(name="關於", value="-----------------------", inline=False)
        embed.add_field(name="s!help",value="指令查詢", inline=False)
        embed.add_field(name="s!about",value="關於微笑小子", inline=False)
        embed.add_field(name="s!info",value="查詢伺服器", inline=False)
        embed.add_field(name="s!ping",value="查詢延遲", inline=False)
        embed.add_field(name="小遊戲", value="-----------------------", inline=False)
        embed.add_field(name="s!fish now",value="釣魚開釣", inline=False)
        embed.add_field(name="s!fish reg",value="釣魚玩家註冊", inline=False)
        embed.add_field(name="s!fish exp",value="釣魚經驗查詢", inline=False)
        # embed.add_field(name="s!dl",value="神社抽籤", inline=False)
        embed.add_field(name="管理使用", value="-----------------------", inline=False)
        embed.add_field(name="s!msgclear + 數量", value="清除數條訊息", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed) #聊天室顯示訊息      

    @commands.command() #查詢伺服器狀態
    async def info(self,ctx):
        await ctx.channel.purge(limit=1)
        server_name = ctx.guild.name
        server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        server_user = len(ctx.guild.members)
        text_channel = len(ctx.guild.text_channels)
        voice_channel = len(ctx.guild.voice_channels)
        # embed 訊息
        embed = discord.Embed(title="我的原始碼", url="https://github.com/minexo79/SmileGuy",color=embedconfig.embed_normal)
        embed.set_thumbnail(url="https://pic.sopili.net/pub/emoji/apple/64/1f9d0.png")
        embed.add_field(name="關於伺服器", value=f"名稱：{server_name}\n創建日期：{server_create_date}\n伺服器人數：{server_user}\n文字頻道：{text_channel}\n語音頻道：{voice_channel}", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(smile(bot))  