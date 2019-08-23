import discord # 導入discord
from discord.ext import commands
import os
import json
import datetime

"""匯入設定檔json 建立jdata"""
with open('setting_interact.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)
with open('setting_disbot.json',mode='r',encoding='utf8') as jfile_bot: #機器人訊息
    jdata_bot = json.load(jfile_bot)

bot = commands.Bot(command_prefix='..') #指令偵測

"""時間設定"""
time_stamp = datetime.datetime.now()
time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')

"""開機訊息"""
bot_m = '[Bot]'
cmd_message1 = ">> The SmileGuy is Running! V1.1(2019/08/22)"

"""基本功能"""

@bot.event #初始開機
async def on_ready():
    #終端訊息
    os.system('cls')
    print(cmd_message1)
    print(bot_m,time_m)

@bot.command() #ping查詢
async def ping(ctx):
    embed = discord.Embed(color=0xffd300)
    embed.add_field(name="我目前的延遲", value=f"{round(bot.latency*1000)} ms", inline=False)
    embed.set_footer(text="SmileGuy Discord Bot")
    await ctx.send(embed=embed)

@bot.event #加入伺服器
async def on_guild_join(guild):
    channel = bot.get_channel(guild._system_channel_id) # 抓取預設聊天室ID
    embed=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=0xffd300)
    embed.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
    embed.add_field(name="目前版本", value="1.1(20190823)", inline=True)
    embed.add_field(name="機器人作者", value="minexo79", inline=False)
    embed.add_field(name="指令幫助", value="..help", inline=True)
    embed.set_footer(text="SmileGuy Discord Bot")
    await channel.send(embed=embed)

"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def loadp(ctx,extension): #載入模組
   bot.load_extension(f'cmds.{extension}')
   print(bot_m,f"<{extension}> load complete!")
   await ctx.send(f"```http\n模組 {extension} 載入成功!\n```")

@bot.command()
async def unloadp(ctx,extension): #卸載模組
   bot.unload_extension(f'cmds.{extension}')
   print(bot_m,f"<{extension}> unload complete!")
   await ctx.send(f"```http\n模組 {extension} 卸載成功!\n```")

@bot.command()
async def reloadp(ctx,extension): #重裝模組
   bot.reload_extension(f'cmds.{extension}')
   print(bot_m,f"<{extension}> reload complete!")
   await ctx.send(f"```http\n模組 {extension} 重裝成功!\n```")


if __name__ == "__main__": 
    bot.run(jdata_bot['TOKEN'])