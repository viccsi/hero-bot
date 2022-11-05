import discord
import pymongo
from pymongo import MongoClient
from random import *
import urllib.parse
from discord.ext import commands
from os import getenv

bot = commands.Bot(command_prefix = "-", description = "Bot by Vic")
global collection
global mango_url
global cluster
global db
mango_url = "mongodb+srv://Vicsi:RafaVic1!@cluster0.2ohdo.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(mango_url)
db = cluster["HeroData"]
collection = db["new"]

@bot.event
async def on_ready():
    print("Ready !")

#CONNECT
@bot.command()
async def start(ctx):
   global user_id
   global author_id
   author_id = ctx.author.id
   user_id = {"_id": author_id}
   if ctx.author == bot.user:
      return
   if ctx.author.bot:
      return
   user_info = {"_id": author_id, "money": 0, "xp": 0, "ami": 0, "c_f": 0, "c_v": 0, "c_s": 0, "c_p":0, "c_c":0, "alter":None, "capa":None}
   collection.insert_one(user_info)
   await ctx.channel.send("👍 Your account have been created !")
@start.error
async def command_start_error(ctx, error):
   await ctx.channel.send("⚠️ Your account have already been created !")

#COMMANDS   
@bot.command()
async def commands(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COMMANDS ⚙️")
    embed.add_field(name="-start", value="Pour commencer l'aventure!", inline=False)
    embed.add_field(name="-profil", value="Pour voir votre profil", inline=False)
    embed.add_field(name="-top", value="Pour voir le classement des meilleurs héros", inline=True)
    await ctx.send(embed=embed)
    
#PROFILS
@bot.command()
async def profil(ctx, member:discord.Member=None):
    if member == None:
        author_id = ctx.author.id
        user_id = {"_id": author_id}
        name = await bot.fetch_user(author_id)
    else:
        author_id = member.id
        user_id = {"_id": author_id}
        name=member
    exp = collection.find(user_id)
    for alter in exp:
        cur_alter = alter["alter"] 
    for xp in exp:
        cur_xp = xp["xp"] 
    exp = collection.find(user_id)
    for idol in exp:
        cur_idol = idol["idol"]
    for ami in exp:
        cur_ami = ami["ami"]
    exp = collection.find(user_id)
    for capa in exp:
        cur_capa = capa["capa"]
    exp = collection.find(user_id)
    for c_c in exp:
        cur_c_c = c_c["c_c"]
    for c_s in exp:
        cur_c_s = c_s["c_s"]
    for c_f in exp:
        cur_c_f = c_f["c_f"]
    for c_v in exp:
        cur_c_v = c_v["c_v"]
    for c_p in exp:
        cur_c_p = c_p["c_p"] 
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFIL " f"{name}" " 👤")
    embed.add_field(name="Alter", value=f"{cur_alter}", inline=False)
    embed.add_field(name="Idole", value=f"{cur_idol}", inline=False)
    embed.add_field(name="Expérience", value="Level 1 -> f"{cur_xp}"" /5🔅", inline=False)
    embed.add_field(name="Amitié", value=f"{cur_ami" "💫", inline=True)
    embed.add_field(name="Capacités", value=f"{cur_c_f}" " ⭐ Force\n" f"{cur_c_v}" " ⭐ Vitesse\n" f"{cur_c_s}" " ⭐ Stratégie\n" f"{cur_c_p}" " ⭐ Pouvoir\n" f"{cur_c_c}" " ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value=f"{cur_capa}", inline=True)
    await ctx.send(embed=embed)   
@bot.command()
async def profil1(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFIL 1 ~ Rayyy")
    embed.add_field(name="Alter", value="Solid to Liquid", inline=False)
    embed.add_field(name="Idole", value="The Bright", inline=True)
    embed.add_field(name="Expérience", value="Level 1 ->  4,2/5🔅", inline=True)
    embed.add_field(name="Amitié", value="0,2💫", inline=True)
    embed.add_field(name="Capacités", value="1,1 ⭐ Force\n1,2 ⭐ Vitesse\n0,3 ⭐ Stratégie\n0 ⭐ Pouvoir\n0 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def profil2(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFIL 2 ~ Loujok")
    embed.add_field(name="Alter", value="Heavy Bones", inline=False)
    embed.add_field(name="Idole", value="Dark Light", inline=True)
    embed.add_field(name="Expérience", value="Level 2 ->  0,2/10 🔅", inline=True)
    embed.add_field(name="Amitié", value="0,3 💫", inline=True)
    embed.add_field(name="Capacités", value="1 ⭐ Force\n2 ⭐ Vitesse\n0 ⭐ Stratégie\n0,1 ⭐ Pouvoir\n0,5 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def profil3(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFIL 3 ~ Doud")
    embed.add_field(name="Alter", value="None ❌", inline=False)
    embed.add_field(name="Idole", value="Nod", inline=True)
    embed.add_field(name="Expérience", value="Level 1 ->  2,3/5 🔅", inline=True)
    embed.add_field(name="Amitié", value="0,3 💫", inline=True)
    embed.add_field(name="Capacités", value="0 ⭐ Force\n0 ⭐ Vitesse\n0,5 ⭐ Stratégie\n0 ⭐ Pouvoir\n0 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def profil4(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFIL 4 ~ Jonas")
    embed.add_field(name="Alter", value="Nether Beam", inline=False)
    embed.add_field(name="Idole", value="Fire Tornado", inline=True)
    embed.add_field(name="Expérience", value="Level 2 ->  0,1/10 🔅", inline=True)
    embed.add_field(name="Amitié", value="0,4 💫", inline=True)
    embed.add_field(name="Capacités", value="1 ⭐ Force\n1,1 ⭐ Vitesse\n0,9 ⭐ Stratégie\n0,1 ⭐ Pouvoir\n0,1 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def profil5(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFIL 5 ~ Koske")
    embed.add_field(name="Alter", value="None ❌", inline=False)
    embed.add_field(name="Idole", value="Moonight", inline=True)
    embed.add_field(name="Expérience", value="Level 1 ->  0,8/5 🔅", inline=True)
    embed.add_field(name="Amitié", value="0,3 💫", inline=True)
    embed.add_field(name="Capacités", value="0 ⭐ Force\n0 ⭐ Vitesse\n0,5 ⭐ Stratégie\n0 ⭐ Pouvoir\n0 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)


#TOP
@bot.command()
async def top(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="- CLASSEMENT HEROS -")
    embed.add_field(name="#1: Big Sun", value="90459 pts", inline=False)
    embed.add_field(name="#2: Moonight", value="86808 pts", inline=False)
    embed.add_field(name="#3: Fire Tornado", value="72394 pts", inline=False)
    embed.add_field(name="#4: Dark Light", value="65362 pts", inline=False)
    embed.add_field(name="#5: The Bright", value="62008 pts", inline=False)
    embed.add_field(name="#6: Nod", value="41898 pts", inline=False)
    embed.add_field(name="#7: Teleport Speed", value="40527 pts", inline=False)
    embed.add_field(name="#8: Silver Fist", value="34685 pts", inline=False)
    embed.add_field(name="#9: Counter", value="25825 pts", inline=False)
    embed.add_field(name="#10: Eveillor", value="12421 pts", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def maj(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="LEADERBOARD UPDATE 🆕")
    embed.add_field(name="-top", value="Pour voir le nouveau classement des meilleurs héros", inline=True)
    await ctx.send(embed=embed)

#COMBATS
a=0
b=0
fi=0
Vh=30
Vm=30
e=0
liste = [1, 2, 3]
eroun = "End Round"
life = "❤️"
vs = " VS "
res=0
    
@bot.command()
async def reset_f(ctx):
    embed=discord.Embed(color=0x636363)
    embed.add_field(name="End of the fight ⚙", value="reason -> reset", inline=False)
    await ctx.send(embed=embed)
    global res
    res=1
        
@bot.command()
async def fight(ctx):
    global res
    while res==1:
        global fi
        global e
        global Vh
        global Vm
        fi=0
        e=0
        Vh=30
        Vm=30
        res=res-1   
    fib=fi
    if fib==0:
        print("START")
        e=e+1
        print("R",e)
        fi=fib+1
        roun = "ROUND"
        numéro = e
        embed=discord.Embed(color=0xfd2626)
        embed.set_author(name=f"{roun} {numéro}")
        embed.add_field(name="Choisit une action... ", value="💥 Attaque\n🛡️ Défense\n☄️ Sournoi", inline=False)
        message=await ctx.send(embed=embed)
        await message.add_reaction("💥")
        await message.add_reaction("🛡️")
        await message.add_reaction("☄")
        def checkEmoji(reaction, user):
            return ctx.message.author == user and message.id==reaction.message.id and(str(reaction.emoji) == "💥" or str(reaction.emoji) == "🛡️" or str(reaction.emoji) == "☄")    
        reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
        if reaction.emoji == "💥":
            global a
            a=1
            global liste
            liste = [1, 2, 3]
            b = choice(liste)
            liste.remove(b)
            if a==b:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="💥💥💥 VS 💥💥💥", value="Attaque    -   Attaque", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-5
                Vm=Vm-5
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
            elif a==b/2:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="💥💥💥 VS 🛡️🛡️🛡️",  value="Attaque    -   Défense", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-0
                Vm=Vm+4
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="💥💥💥 VS ☄☄☄", value="Attaque    -   Sournois", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-0
                Vm=Vm-7
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
        elif reaction.emoji == "🛡️":
            a=2
            liste = [1, 2, 3]
            b = choice(liste)
            liste.remove(b)
            if a==b*2:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="🛡️🛡️🛡️ VS 💥💥💥", value="Défense    -   Attaque", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh+4
                Vm=Vm-0
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
            elif a==b:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="🛡️🛡️🛡️ VS 🛡️🛡️🛡️", value="Défense    -   Défense", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh+1
                Vm=Vm+1
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="🛡️🛡️🛡️ VS ☄☄☄", value="Défense    -   Sournois", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-8
                Vm=Vm-0
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
        else:
            a=3
            liste = [1, 2, 3]
            b = choice(liste)
            liste.remove(b)
            if a==b*3:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="☄☄☄ VS 💥💥💥", value="Sournois    -   Attaque", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-7
                Vm=Vm-0
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
            elif a==b:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="☄☄☄ VS ☄☄☄", value="Sournois    -   Sournois", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-3
                Vm=Vm-3
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name="☄☄☄ VS 🛡️🛡️🛡️", value="Sournois    -   Défense", inline=False)
                await ctx.send(embed=embed)
                Vh=Vh-0
                Vm=Vm-8
                embed=discord.Embed(color=0xfd2626)
                embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                await ctx.send(embed=embed)
    else:
        if Vh>0 and Vm>0:
            e=e+1
            print("R",e)
            if a==1:
                roun = "ROUND"
                numéro = e
                embed=discord.Embed(color=0xfd2626)
                embed.set_author(name=f"{roun} {numéro}")
                embed.add_field(name="Choisit une action... ", value="~~💥 Attaque~~\n🛡️ Défense\n☄️ Sournoi", inline=False)
                message=await ctx.send(embed=embed)
                await message.add_reaction("🛡️")
                await message.add_reaction("☄")
                def checkEmoji(reaction, user):
                    return ctx.message.author == user and message.id==reaction.message.id and(str(reaction.emoji) == "💥" or str(reaction.emoji) == "🛡️" or str(reaction.emoji) == "☄")
                reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)    
                if reaction.emoji == "🛡️":
                    a=2
                    b = choice(liste)
                    liste = [1, 2, 3]
                    liste.remove(b)
                    if a==b*2:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="🛡️🛡️🛡️ VS 💥💥💥", value="Défense    -   Attaque", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh+4
                        Vm=Vm-0
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    elif a==b:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="🛡️🛡️🛡️ VS 🛡️🛡️🛡️", value="Défense    -   Défense", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh+1
                        Vm=Vm+1
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="🛡️🛡️🛡️ VS ☄☄☄", value="Défense    -   Sournois", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-8
                        Vm=Vm-0
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                else:
                    a=3
                    b = choice(liste)
                    liste = [1, 2, 3]
                    liste.remove(b)
                    if a==b*3:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="☄☄☄ VS 💥💥💥", value="Sournois    -   Attaque", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-7
                        Vm=Vm-0
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    elif a==b:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="☄☄☄ VS ☄☄☄", value="Sournois    -   Sournois", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-3
                        Vm=Vm-3
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="☄☄☄ VS 🛡️🛡️🛡️", value="Sournois    -   Défense", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-0
                        Vm=Vm-8
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
            elif a==2:
                roun = "ROUND"
                numéro = e
                embed=discord.Embed(color=0xfd2626)
                embed.set_author(name=f"{roun} {numéro}")
                embed.add_field(name="Choisit une action... ", value="💥 Attaque\n~~🛡️ Défense~~\n☄️ Sournoi", inline=False)
                message=await ctx.send(embed=embed)
                await message.add_reaction("💥")
                await message.add_reaction("☄")
                def checkEmoji(reaction, user):
                    return ctx.message.author == user and message.id==reaction.message.id and(str(reaction.emoji) == "💥" or str(reaction.emoji) == "🛡️" or str(reaction.emoji) == "☄")    
                reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
                if reaction.emoji == "💥":
                    a=1
                    b = choice(liste)
                    liste = [1, 2, 3]
                    liste.remove(b)
                    if a==b:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="💥💥💥 VS 💥💥💥", value="Attaque    -   Attaque", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-5
                        Vm=Vm-5
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    elif a==b/2:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="💥💥💥 VS 🛡️🛡️🛡️", value="Attaque    -   Défense", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-0
                        Vm=Vm+4
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="💥💥💥 VS ☄☄☄", value="Attaque    -   Sournois", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-0
                        Vm=Vm-7
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                else:
                    a=3
                    b = choice(liste)
                    liste = [1, 2, 3]
                    liste.remove(b)
                    if a==b/3:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="☄☄☄ VS 💥💥💥", value="Sournois    -   Attaque", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-7
                        Vm=Vm-0
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    elif a==b:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="☄☄☄ VS ☄☄☄", value="Sournois    -   Sournois", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-3
                        Vm=Vm-3
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="☄☄☄ VS 🛡️🛡️🛡️", value="Sournois    -   Défense", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-0
                        Vm=Vm-8
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
            else:
                roun = "ROUND"
                numéro = e
                embed=discord.Embed(color=0xfd2626)
                embed.set_author(name=f"{roun} {numéro}")
                embed.add_field(name="Choisit une action... ", value="💥 Attaque\n🛡️ Défense\n~~☄️ Sournoi~~", inline=False)
                message=await ctx.send(embed=embed)
                await message.add_reaction("💥")
                await message.add_reaction("🛡️")
                def checkEmoji(reaction, user):
                    return ctx.message.author == user and message.id==reaction.message.id and(str(reaction.emoji) == "💥" or str(reaction.emoji) == "🛡️" or str(reaction.emoji) == "☄")    
                reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
                if reaction.emoji == "💥":
                    a=1
                    b = choice(liste)
                    liste = [1, 2, 3]
                    liste.remove(b)
                    if a==b:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="💥💥💥 VS 💥💥💥", value="Attaque    -   Attaque", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-5
                        Vm=Vm-5
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    elif a==b/2:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="💥💥💥 VS 🛡️🛡️🛡️", value="Attaque    -   Défense", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-0
                        Vm=Vm+4
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="💥💥💥 VS ☄☄☄", value="Attaque    -   Sournois", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-0
                        Vm=Vm-7
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                else:
                    a=2
                    b = choice(liste)
                    liste = [1, 2, 3]
                    liste.remove(b)
                    if a==b*2:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="🛡️🛡️🛡️ VS 💥💥💥", value="Défense    -   Attaque", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh+4
                        Vm=Vm-0
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    elif a==b:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="🛡️🛡️🛡️ VS 🛡️🛡️🛡️", value="Défense    -   Défense", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh+4
                        Vm=Vm+4
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name="🛡️🛡️🛡️ VS ☄☄☄", value="Défense    -   Sournois", inline=False)
                        await ctx.send(embed=embed)
                        Vh=Vh-8
                        Vm=Vm-0
                        embed=discord.Embed(color=0xfd2626)
                        embed.add_field(name=f"{Vh} {life} {vs} {life} {Vm}", value=f"{eroun} {numéro}", inline=False)
                        await ctx.send(embed=embed)
        elif Vh<0 and Vm>0:
            embed=discord.Embed(color=0xc20000)
            embed.add_field(name="COUP FATAL", value="Tu as été vaincu...", inline=False)
            await ctx.send(embed=embed)
            fi=0
            e=0
            Vh=30
            Vm=30
            print("Loose...")
        elif Vh>0 and Vm<0:
            embed=discord.Embed(color=0x0fd730)
            embed.add_field(name="COUP FATAL", value="Tu as vaincu.", inline=False)
            await ctx.send(embed=embed)
            fi=0
            e=0
            Vh=30
            Vm=30
            print("Win !")
        else:
            embed=discord.Embed(color=0xfd2626)
            embed.add_field(name="TIE", value="ex-aequo", inline=False)
            await ctx.send(embed=embed)
            fi=0
            e=0
            Vh=30
            Vm=30
            print("Tie")
    

bot.run(getenv('TOKEN'))

