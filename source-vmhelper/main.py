import discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands
import os
from webserver import keep_alive

bot = commands.Bot(command_prefix='>') #指令偵測
bot.remove_command('help') #刪除help
bot_m = "[VM]"

@bot.event #開機
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game("幫助：>help")) #bot狀態
    os.system('clear')
    print(bot_m,"booting successful.")

@bot.event #錯誤的指令
async def on_command_error(ctx,error):
    if isinstance(error,CommandNotFound) and ctx.author != bot.user:
        await ctx.send("嗯?我看不懂啊......")

"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def reload(ctx,extension): #重裝模組
    bot.reload_extension(f'cmds.{extension}')
    print(bot_m,f"<{extension}> reload complete.")
    await ctx.send(f"```css\n模組 {extension} 已重裝。\n```")

if __name__ == "__main__":
    keep_alive()
    bot.run(f"",bot=True,reconnect=True)