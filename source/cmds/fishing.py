import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import asyncio
import embedconfig
import MySQLdb

class fishing(Cog_Extension):
    """釣魚"""

    @commands.command() #釣魚
    async def fish(self,ctx,feature:str):

        conn = MySQLdb.connect(
            host="",
            user="",
            passwd="",
            database=""
        )

        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS smileguy_fishing (user_id VARCHAR(255), exp FLOAT(255,1))")
        nologin = 0;  
        if feature == 'exp': # 查詢經驗
            sql = f"SELECT * FROM smileguy_fishing"
            c.execute(sql)
            myresult = c.fetchall()
            for row in myresult:
                user_id = row[0]
                exp = row[1]
                if str(ctx.message.author.id) == str(user_id): # 有註冊
                    nologin = 0;
                    ## Embed
                    embed = discord.Embed(color=embedconfig.color)
                    embed.add_field(name='玩家', value=f"{ctx.message.author.mention}\n({user_id})", inline=False)
                    embed.add_field(name='經驗值', value="%s" % (exp), inline=False)
                    embed.set_footer(text=embedconfig.footer)
                    await ctx.send(embed=embed)     
                    conn.close() 
                    break    
                else: # 沒註冊
                    nologin = nologin + 1; 

            if(nologin != 0):
                await ctx.send("還沒註冊喔~'\n註冊指令:`fish reg`")
                conn.close()

        elif feature == 'reg': # 註冊
            sql = "SELECT * FROM smileguy_fishing"
            c.execute(sql)
            myresult = c.fetchall()
            for row in myresult:
                user_id = row[0]
                if str(ctx.message.author.id) != str(user_id): # 沒註冊
                    nologin = 0
                else: # 有註冊 
                    nologin = nologin + 1
                    break

            if(nologin != 0):
                await ctx.send("註冊過了喔~")
                conn.close()
            else:
                sql = "INSERT INTO smileguy_fishing (user_id, exp) VALUES (%s,%s)"
                val = (f"{ctx.message.author.id}", "0.0")
                c.execute(sql, val)
                conn.commit()      
                await ctx.send("釣魚功能註冊成功!!")
                conn.close()    

        elif feature == 'now': # 釣魚
            #SQl Search user
            sql = "SELECT * FROM smileguy_fishing"
            c.execute(sql)
            myresult = c.fetchall()
            for row in myresult:
                user_id = row[0]
                exp = row[1]
                if str(ctx.message.author.id) == str(user_id): # 有註冊
                    nologin = 0;  
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
                        exp2 = exp + 1.5
                        sql = "UPDATE smileguy_fishing SET exp = %s WHERE user_id = %s"
                        val = (f"{exp2}",f"{ctx.message.author.id}")
                        c.execute(sql, val)
                        conn.commit()  
                        #Embed
                        file = discord.File(".//pic//fishing//shark.png",filename="shark.png") #調出本地圖片
                        attachment = "attachment://shark.png" #embed指標
                        embed = discord.Embed(color=embedconfig.color)
                        embed.set_image(url=attachment)
                        embed.add_field(name='結果', value=f"{user}\n釣到 __**大白鯊**__ !!!\n`經驗值 + 1.5`", inline=False)
                        embed.set_footer(text=embedconfig.footer)
                        await ctx.send(file=file,embed=embed)         
                        conn.close()
                        break

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
                        exp2 = exp + 1.0
                        sql = "UPDATE smileguy_fishing SET exp = %s WHERE user_id = %s"
                        val = (f"{exp2}",f"{ctx.message.author.id}")
                        c.execute(sql, val)
                        conn.commit()  
                        #Embed
                        embed = discord.Embed(color=embedconfig.color)
                        embed.set_thumbnail(url=attachment)
                        embed.add_field(name='結果', value=f"恭喜{user}\n釣到一隻 __**{random_mes}**__ !!!\n`經驗值 + 1.0`", inline=False)
                        embed.set_footer(text=embedconfig.footer)
                        await ctx.send(file=file,embed=embed)
                        conn.close()
                        break                    

                    elif fish_val >= 0.2 and fish_val < 0.5: #釣到垃圾
                        exp2 = exp + 0.5
                        sql = "UPDATE smileguy_fishing SET exp = %s WHERE user_id = %s"
                        val = (f"{exp2}",f"{ctx.message.author.id}")
                        c.execute(sql, val)
                        conn.commit()  
                        #Embed
                        file = discord.File(".//pic//fishing//bone.png",filename="bone.png") #調出本地圖片
                        attachment = "attachment://bone.png" #embed指標            
                        embed = discord.Embed(color=embedconfig.color)
                        embed.set_thumbnail(url=attachment)
                        embed.add_field(name='結果', value=f"{user}\n釣到了一坨 __**垃圾**__ !!!\n`經驗值 + 0.5`", inline=False)
                        embed.set_footer(text=embedconfig.footer)
                        await ctx.send(file=file,embed=embed)
                        conn.close()
                        break

                    else: #沒釣到
                        ## Embed
                        embed = discord.Embed(color=embedconfig.color)
                        embed.add_field(name='結果', value=f"{user}\n甚麼也沒有釣到......", inline=False)
                        embed.set_footer(text=embedconfig.footer)
                        await ctx.send(embed=embed)  
                        conn.close()
                        break

                else: # 沒註冊
                    nologin = nologin + 1;

            if(nologin != 0):
                await ctx.send("還沒註冊喔~'\n註冊指令:`fish reg`")
                conn.close()
        else:
            embed = discord.Embed(color=embedconfig.color)
            embed.add_field(name="訊息", value="**訊息輸入錯誤**", inline=False)
            embed.set_footer(text=embedconfig.footer)   
            await ctx.send(embed=embed)  
            conn.close()
                
def setup(bot):
    bot.add_cog(fishing(bot))       
