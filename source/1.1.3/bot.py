import discord # 導入discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands,tasks
import os
import json
import datetime

"""匯入設定檔json 建立jdata"""
with open('setting_react.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)

bot = commands.Bot(command_prefix='!') #指令偵測
bot.remove_command('help') #刪除help

"""時間設定"""
time_stamp = datetime.datetime.now()
time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')

"""開機訊息"""
bot_m = '[Bot]'
cmd_message1 = ">> SmileGuy Running! V1.1.3(2019/08/26)"

"""顏色"""
blue_text = "in \033[34m"

"""基本功能"""

@bot.event #初始開機
async def on_ready():
    #終端訊息
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game('SmileGuy Running! V1.1.3')) #bot狀態
    os.system('cls') #windows專用
    print(cmd_message1)
    print(bot_m,time_m)

@bot.event #加入伺服器
async def on_guild_join(guild):
    embed=discord.Embed(title="我的原始碼: https://github.com/minexo79/SmileGuy", url="https://github.com/minexo79/SmileGuy",color=0xffd300)
    embed.set_author(name="😀😀謝謝你加我進伺服器，我是微笑小子!!😆😆")
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/04/01/09/07/wink-98461_960_720.png")
    embed.add_field(name="目前版本", value="1.1.3(20190826)", inline=True)
    embed.add_field(name="機器人作者", value="minexo79", inline=False)
    embed.add_field(name="指令幫助", value="!help", inline=True)
    embed.set_footer(text="SmileGuy Discord Bot")
    channel = bot.get_channel(guild._system_channel_id) # 抓取預設聊天室ID
    print(bot_m,"joined at",guild.name,blue_text,time_m) #抓取伺服器名稱並且印在CLR上面
    await channel.send(embed=embed) #聊天室顯示加入訊息

@bot.event #錯誤的指令
async def on_command_error(ctx,error):
    while isinstance(error,CommandNotFound):
        embed = discord.Embed(color=0xffd300)
        embed.add_field(name="訊息", value="**訊息輸入錯誤**", inline=False)
        embed.set_footer(text="SmileGuy Discord Bot")   
        await ctx.send(embed=embed)

"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def load(ctx,extension): #載入模組
    bot.load_extension(f'cmds.{extension}')
    print(bot_m,f"<{extension}> load complete!")
    await ctx.send(f"```http\n模組 {extension} 載入成功!\n```")

@bot.command()
async def unload(ctx,extension): #卸載模組
    bot.unload_extension(f'cmds.{extension}')
    print(bot_m,f"<{extension}> unload complete!")
    await ctx.send(f"```http\n模組 {extension} 卸載成功!\n```")

@bot.command()
async def reload(ctx,extension): #重裝模組
    bot.reload_extension(f'cmds.{extension}')
    print(bot_m,f"<{extension}> reload complete!")
    await ctx.send(f"```http\n模組 {extension} 重裝成功!\n```")

if __name__ == "__main__": 
    bot.run()