import discord # 導入discord
from discord.ext import commands
import os
import json
import datetime

#匯入設定檔json 建立jdata
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='..') #指令偵測

time_stamp = datetime.datetime.now()
time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')

bot_m = '[Bot]'

#開機訊息
cmd_message1 = "(● SmileGuy Discord Robot --V1.0(2019/08/20)"
cmd_message2 = " (● Made By: Tsai XO\n"
cmd_message3 = "The SmileGuy is Running!"
cmd_message4 = "Open Time:"
cmd_message5 = "Now Ping:"

#顏色設定
red_F = "\033[31m" #紅色
green_F = "\033[32m" #綠色
yellow_F = "\033[33m" #黃色
blue_F = "\033[36m" #淺藍色
white_F = "\033[0m" #白色

@bot.event #初始開機
async def on_ready():
    #終端訊息
    os.system('cls')
    print(green_F,cmd_message1)
    print(cmd_message2,white_F)
    print(bot_m,blue_F,cmd_message3,white_F)
    print(bot_m,blue_F,cmd_message4,time_m,white_F)
    print(bot_m,blue_F,cmd_message5,round(bot.latency*1000),white_F)
    #頻道發言
    mschannel = bot.get_channel(int(jdata['msg_channel'])) #指定聊天頻道
    await mschannel.send(jdata['chat_message1'])

@bot.event #成員加入
async def on_member_join(member):
    #終端訊息
    print(bot_m,(member),jdata['cmd_message_join'],time_m)
    #頻道發言
    mschannel = bot.get_channel(int(jdata['welcome_channel'])) #指定聊天頻道
    await mschannel.send(f"{member.mention}",jdata['chat_message_join'])
    
@bot.event #成員離開
async def on_member_remove(member):
    #終端訊息
    print(bot_m,(member),jdata['cmd_message_leave'],time_m)

@bot.command() #ping查詢
async def botping(ctx):
    await ctx.send(f"```css\n[我目前的延遲為: {round(bot.latency*1000)} ms.]\n```")

@bot.command() #HELP
async def bothelp(ctx):
    await ctx.send(jdata['chat_bothelp'])

bot.run(jdata['TOKEN'])