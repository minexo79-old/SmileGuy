from flask import Flask
from threading import Thread
import json

"""匯入設定檔json 建立jdata"""
with open('setting_bot.json',mode='r',encoding='utf8') as jfile_bot: #機器人設定檔
    jdata_bot = json.load(jfile_bot)


app = Flask('')

@app.route('/')
def home():
    return "Smile is run."

def run():
    app.run(host="0.0.0.0",port=8080)

def keep_alive():
    t=Thread(target=run)
    t.start()
