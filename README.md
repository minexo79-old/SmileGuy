# SmileGuy 微笑小子
[![Python 3.7.4](https://img.shields.io/badge/Python-3.7.4-blue?style=flat&logo=python)](https://www.python.org/downloads/release/python-374/)
![Discord.py](https://img.shields.io/badge/discord.py-1.2.5-blue?style=flat&logo=discord)
![Online](https://img.shields.io/badge/Status-Running-brightgreen)
![commit-activity](https://img.shields.io/github/last-commit/minexo79/SmileGuy?style=flat-square)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![issue](https://img.shields.io/bitbucket/issues-raw/minexo79/smileguy?style=social)

我是微笑小子，這是我的主人為我運作的程式碼。  
[將SmileGuy加到你的伺服器](https://discordapp.com/api/oauth2/authorize?client_id=613249451355799552&permissions=8&scope=bot)  

#### 尚未完成功能：  
- [ ] 釣魚：不同釣竿、寶箱
- [ ] 跨服更新通知推送
- [ ] 自訂回應

## 建置環境：
`python 3.7.4`
`discord.py 1.2.5`
`mysqlclient`
`一台可以跑的電腦(X`

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
2. 打開`bot.py`之後機器人就會自動運行。
3. `setting_react.json`內有道「早」的回應，可以自行更改。  

## 管理指令：
* 模組裝載(僅權限擁有者使用):  
  * 載入: `s!load` <模組>
  * 卸載: `s!unload` <模組>
  * 重載: `s!reload` <模組>
* 刪除聊天紀錄:
  * `s!msgclear` <欲刪除訊息個數>
