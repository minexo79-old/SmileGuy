# SmileGuy 微笑小子

[![Python 3.7.4](https://img.shields.io/badge/Python-3.7.4-blue?style=flat&logo=python)](https://www.python.org/downloads/release/python-374/)
![Discord.py](https://img.shields.io/badge/discord.py-1.2.5-blue?style=flat&logo=discord)
![Online](https://img.shields.io/badge/Status-Running-brightgreen)
![commit-activity](https://img.shields.io/github/last-commit/minexo79/SmileGuy?style=flat-square)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![issue](https://img.shields.io/bitbucket/issues-raw/minexo79/smileguy?style=social)

---

我是微笑小子，這是我的主人為我運作的程式碼。  
[將SmileGuy加到你的伺服器](https://discordapp.com/api/oauth2/authorize?client_id=613249451355799552&permissions=8&scope=bot) 

---

## 開發者＆合作夥伴：      
|(開發者) minexo79|(繪師) Vtuber雙命裂#1716|(繪師) SAIFRIX#1996|
|:--------------:|:---------------------:|:-----------------:|
|[![minexo79](https://avatars0.githubusercontent.com/u/54303621?s=128&v=4)](https://github.com/minexo79)|[![doublemin](https://yt3.ggpht.com/a/AGF-l78DFH5aR25qUjbbwxSAtbPwhMLAxuYK4BJFxg=s128-c-k-c0xffffffff-no-rj-mo)](https://www.youtube.com/channel/UCtKyM4DA8CyCAm5LGsvUsag)|![SAIFRIX](https://cdn.discordapp.com/avatars/484671733987803177/ef4f5dc3e0956fb9bf9fe043b249d467.png?size=128)|
 
---

#### 尚未完成的功能：  
- [ ] 釣魚：不同釣竿、寶箱
- [ ] 跨服更新通知推送
- [ ] 自訂回應
- [ ] 神社抽籤
 
---

## 建置環境：
- [x] 一台可以跑的電腦
- [x] python 3.7.4 或更高
- [x] discord.py 1.3.1
- [x] mysqlclient
 
---

## 建置步驟：
1. 將`setting_bot-example.json`改名成`setting_bot.json`並填入以下資料：
```js
{
	"Token" : "在Discord Developer Portal獲取的TOKEN",
	"SQLserver": "你的MySQL伺服器",
	"User":"MySQL使用者",
	"Passwd":"MySQL密碼",
	"Database":"指定資料庫",
	"Owner":"權限擁有者"
}
```
2. 點兩下`bot.py`之後機器人就會自動運行。
3. `setting_react.json`內有道「早」的回應，可以自行更改。  
 
---

## 管理指令：
* 模組裝載 (**僅權限擁有者使用**):  
  * 載入: `s!load` <模組>
  * 卸載: `s!unload` <模組>
  * 重載: `s!reload` <模組>
* 刪除聊天紀錄 (**僅限管理員使用**):
  * `s!clear` <欲刪除訊息個數>
