import discord # 導入discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands,tasks
import os
import json
import datetime

"""匯入設定檔json 建立jdata"""
with open('setting_react.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #機器人設定檔
    jdata_bot = json.load(jfile_bot)

bot = commands.Bot(command_prefix='!') #指令偵測
bot.remove_command('help') #刪除help

"""開機訊息"""
bot_m = '[Bot]'
cmd_message1 = ">> SmileGuy Running! V1.2(2019/09/03)"

"""基本功能"""

@bot.event #初始開機
async def on_ready():
    """時間設定"""
    time_stamp = datetime.datetime.now()
    time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
    #終端訊息
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(jdata_bot['Status'])) #bot狀態
    os.system('cls') #windows專用
    print(cmd_message1)
    print(bot_m,time_m)

@bot.event #錯誤的指令
async def on_command_error(ctx,error):
    if isinstance(error,CommandNotFound) and ctx.author != bot.user:
        embed = discord.Embed(color=0xffd300)
        embed.add_field(name="訊息", value="**訊息輸入錯誤**", inline=False)
        embed.set_footer(text="SmileGuy Discord Bot")   
        await ctx.send(embed=embed)

"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

# @bot.command()
# async def load(ctx,extension): #載入模組
#     bot.load_extension(f'cmds.{extension}')
#     print(bot_m,f"<{extension}> load complete!")
#     await ctx.send(f"```http\n模組 {extension} 載入成功!\n```")

# @bot.command()
# async def unload(ctx,extension): #卸載模組
#     bot.unload_extension(f'cmds.{extension}')
#     print(bot_m,f"<{extension}> unload complete!")
#     await ctx.send(f"```http\n模組 {extension} 卸載成功!\n```")

@bot.command()
async def reload(ctx,extension): #重裝模組
    bot.reload_extension(f'cmds.{extension}')
    print(bot_m,f"<{extension}> reload complete!")
    await ctx.send(f"```http\n模組 {extension} 重裝成功!\n```")

if __name__ == "__main__": 
    bot.run(jdata_bot[f"Token"])