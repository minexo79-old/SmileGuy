import discord # 導入discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands,tasks
import os
import json
import datetime
import pytz

tz = pytz.timezone('Asia/Taipei')

"""匯入設定檔json 建立jdata"""
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #機器人設定檔
    jdata_bot = json.load(jfile_bot)

bot = commands.Bot(command_prefix='s!') #指令偵測
bot.remove_command('help') #刪除help

"""開機訊息"""
bot_m = '[Bot]'

"""基本功能"""

@bot.event #初始開機
async def on_ready():
    """時間設定"""
    time_stamp = datetime.datetime.now(tz)
    time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
    #終端訊息
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(jdata_bot['Status'])) #bot狀態
    os.system('clear') #linux專用
    print(jdata_bot['Cmd_message'])
    print(bot_m,time_m)

"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata_bot[f"Token"],bot=True,reconnect=True)