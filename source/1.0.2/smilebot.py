import discord # 導入discord
from discord.ext import commands
import os
import json
import datetime
import random

#匯入設定檔json 建立jdata
with open('setting_interact.json',mode='r',encoding='utf8') as jfile_in: #互動設定檔
    jdata_in = json.load(jfile_in)
with open('setting_disbot.json',mode='r',encoding='utf8') as jfile_bot: #機器人訊息
    jdata_bot = json.load(jfile_bot)
with open('setting_chatphoto.json',mode='r',encoding='utf8') as jfile_chatphoto: #機器人訊息
    jdata_chatphoto = json.load(jfile_chatphoto)

bot = commands.Bot(command_prefix='..') #指令偵測

#時間設定
time_stamp = datetime.datetime.now()
time_m = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')

#開機訊息
bot_m = '[Bot]'
cmd_message1 = "(● SmileGuy Discord Robot --V1.0.1(2019/08/21)"
cmd_message2 = "(● Made By: Tsai XO\n"
cmd_message3 = "The SmileGuy is Running!"
cmd_message4 = "Open Time:"
cmd_message5 = "Now Ping:"
cmd_message6 = "add a photo: "
cmd_message7 = "delete a photo: "

#基本功能

@bot.event #初始開機
async def on_ready():
    #終端訊息
    os.system('cls')
    print(cmd_message1)
    print(cmd_message2)
    print(bot_m,cmd_message3)
    print(bot_m,cmd_message4,time_m)
    print(bot_m,cmd_message5,round(bot.latency*1000))
    #頻道發言
    mschannel = bot.get_channel(int(jdata_bot['msg_channel'])) #指定聊天頻道
    await mschannel.send(jdata_in['chat_message_startup'])
    await mschannel.send(jdata_in['chat_bothelp'])

@bot.event #成員加入
async def on_member_join(member):
    #終端訊息
    print(bot_m,(member),jdata_in['cmd_message_join'],time_m)
    #頻道發言
    mschannel = bot.get_channel(int(jdata_bot['welcome_channel'])) #指定聊天頻道
    await mschannel.send(f"{member.mention}",jdata_in['chat_message_join'])
    
@bot.event #成員離開
async def on_member_remove(member):
    #終端訊息
    print(bot_m,(member),jdata_in['cmd_message_leave'],time_m)

@bot.command() #ping查詢
async def botping(ctx):
    await ctx.send(f"```css\n[我目前的延遲為: {round(bot.latency*1000)} ms.]\n```")
    print(bot_m,cmd_message5,round(bot.latency*1000))

@bot.command() #HELP
async def bothelp(ctx):
    await ctx.send(jdata_in['chat_bothelp'])

#娛樂功能

@bot.command() #發梗圖
async def photo(ctx):
    random_pic = random.choice(jdata_chatphoto['chat_photo']) #隨機選取網址
    # pic = discord.File(random_pic) #本機端專用
    await ctx.send(random_pic) #發送隨機圖片

@bot.command() #加梗圖
async def addphoto(ctx,msg):
    wr = jdata_chatphoto['chat_photo'] #指定元素
    wr.append(msg) #增加網址
    with open('setting_chatphoto.json',mode='w',encoding='utf8') as jsave: #權限改成寫入
        data = {
            "chat_photo":wr #格式
        }
        json.dump(data,jsave) #存檔
        print(bot_m,ctx.message.author,cmd_message6,msg) #CLS畫面
        await ctx.send(jdata_in['chat_photo_add']) #聊天室

@bot.command() #刪梗圖
async def delphoto(ctx,msg):
    wr = jdata_chatphoto['chat_photo'] #指定元素
    wr.remove(msg) #刪除網址
    with open('setting_chatphoto.json',mode='w',encoding='utf8') as jsave: #權限改成寫入
        data = {
            "chat_photo":wr #格式
        }
        json.dump(data,jsave) #存檔
        print(bot_m,ctx.message.author,cmd_message7,msg) #CLS畫面
        await ctx.send(jdata_in['chat_photo_del']) #聊天室

bot.run(jdata_bot['TOKEN'])