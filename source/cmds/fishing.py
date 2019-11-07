import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import asyncio
import embedconfig

class fishing(Cog_Extension):
    """釣魚"""

    @commands.command() #釣魚
    async def fish(self,ctx):
        ## Embed
        user = ctx.message.author.mention
        file = discord.File(".//pic//fishing//fish.gif",filename="fish.gif") #調出本地圖片
        embed = discord.Embed(color=embedconfig.color)
        embed.set_thumbnail(url="attachment://fish.gif") #embed指標
        embed.add_field(name='釣魚', value=f"{user} 揮了魚竿，\n坐在河邊的石頭等待魚兒的到來。", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(file=file,embed=embed)
        #隨機延遲秒數(5~10秒)
        time = random.randint(5,10)
        await asyncio.sleep(time)
        fish_val = random.uniform(0,1.5)

        if fish_val >= 1.2: # 大白鯊
            file = discord.File(".//pic//fishing//shark.png",filename="shark.png") #調出本地圖片
            attachment = "attachment://shark.png" #embed指標
            embed = discord.Embed(color=embedconfig.color)
            embed.set_image(url=attachment)
            embed.add_field(name='結果', value=f"你釣到 __**大白鯊**__ !!!", inline=False)
            embed.set_footer(text=embedconfig.footer)
            await ctx.send(file=file,embed=embed)            
        
        elif fish_val >= 0.5 and fish_val < 1.2: #一般魚
            ## Embed
            fish = ["鱈魚","鮭魚","河豚","熱帶魚"]
            random_mes=random.choice(fish)

            if random_mes == "鱈魚":
                file = discord.File(".//pic//fishing//row_cod.png",filename="row_cod.png")
                attachment = "attachment://row_cod.png"

            elif random_mes == "鮭魚":
                file = discord.File(".//pic//fishing//row_salmon.png",filename="row_salmon.png")
                attachment = "attachment://row_salmon.png"

            elif random_mes == "河豚":
                file = discord.File(".//pic//fishing//pufferfish.png",filename="pufferfish.png")
                attachment = "attachment://pufferfish.png"

            elif random_mes == "熱帶魚":
                file = discord.File(".//pic//fishing//tropical_fish.png",filename="tropical_fish.png") #調出本地圖片
                attachment = "attachment://tropical_fish.png" #embed指標

            embed = discord.Embed(color=embedconfig.color)
            embed.set_thumbnail(url=attachment)
            embed.add_field(name='結果', value=f"恭喜釣到一隻 __**{random_mes}**__ !!!", inline=False)
            embed.set_footer(text=embedconfig.footer)
            await ctx.send(file=file,embed=embed)
            # 寫入json檔案
        
        elif fish_val >= 0.2 and fish_val < 0.5: #釣到垃圾
            file = discord.File(".//pic//fishing//bone.png",filename="bone.png") #調出本地圖片
            attachment = "attachment://bone.png" #embed指標            
            embed = discord.Embed(color=embedconfig.color)
            embed.set_thumbnail(url=attachment)
            embed.add_field(name='結果', value=f"釣到了一坨 __**垃圾**__ !!!", inline=False)
            embed.set_footer(text=embedconfig.footer)
            await ctx.send(file=file,embed=embed)

        else: #沒釣到
            ## Embed
            embed = discord.Embed(color=embedconfig.color)
            embed.add_field(name='結果', value="甚麼也沒有釣到......", inline=False)
            embed.set_footer(text=embedconfig.footer)
            await ctx.send(embed=embed)           

def setup(bot):
    bot.add_cog(fishing(bot))       
