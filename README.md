# SmileGuy
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-367/)

我是微笑小子，這是我的主人為我運作的程式碼。  

[將SmileGuy加到你的伺服器](https://discordapp.com/api/oauth2/authorize?client_id=613249451355799552&permissions=8&scope=bot)  

* 使用前先在`setting_bot.json`填入以下資料：
```js
{
	"Token" : "在Discord Developer Portal獲取的TOKEN",
        "SQLserver": "你的MySQL伺服器",
        "User":"MySQL使用者",
   	"Passwd":"MySQL密碼",
   	"Database":"指定資料表",
	"Owner":"權限擁有者"
}
```

* 模組裝載指令:  
  * 載入: s!load <模組>
  * 卸載: s!unload <模組>
  * 重載: s!reload <模組>
