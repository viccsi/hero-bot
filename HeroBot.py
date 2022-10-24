import discord
from discord.ext import commands
from os import getenv

bot = commands.Bot(command_prefix = "-", description = "Bot by Vic")

@bot.event
async def on_ready():
    print("Ready !")
    
@bot.command()
async def commands(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COMMANDS ⚙️")
    embed.add_field(name="-profile", value="Pour voir votre profil `-profile[numéro]`", inline=False)
    embed.add_field(name="-top", value="Pour voir le classement des meilleurs héros", inline=True)
    await ctx.send(embed=embed)
    
@bot.command()
async def profile1(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFILE 1 ~ Rayyy")
    embed.add_field(name="Alter", value="Solid to Liquid", inline=False)
    embed.add_field(name="Idole", value="The Bright", inline=True)
    embed.add_field(name="Expérience", value="Level 1 ->  4,2/5🔅", inline=True)
    embed.add_field(name="Amitié", value="0,2💫", inline=True)
    embed.add_field(name="Capacités", value="1,1 ⭐ Force\n1,2 ⭐ Vitesse\n0,3 ⭐ Stratégie\n0 ⭐ Pouvoir\n0 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def profile2(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFILE 2 ~ Loujok")
    embed.add_field(name="Alter", value="Heavy Bones", inline=False)
    embed.add_field(name="Idole", value="Dark Light", inline=True)
    embed.add_field(name="Expérience", value="Level 2 ->  0/10 🔅", inline=True)
    embed.add_field(name="Amitié", value="0,3 💫", inline=True)
    embed.add_field(name="Capacités", value="1 ⭐ Force\n2 ⭐ Vitesse\n0 ⭐ Stratégie\n0 ⭐ Pouvoir\n0,5 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)
@bot.command()
async def profile3(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="PROFILE 3 ~ Doud")
    embed.add_field(name="Alter", value="None ❌", inline=False)
    embed.add_field(name="Idole", value="None ❌", inline=True)
    embed.add_field(name="Expérience", value="Level 1 ->  0/5 🔅", inline=True)
    embed.add_field(name="Amitié", value="0 💫", inline=True)
    embed.add_field(name="Capacités", value="0 ⭐ Force\n0 ⭐ Vitesse\n0 ⭐ Stratégie\n0 ⭐ Pouvoir\n0 ⭐ Courage", inline=False)
    embed.add_field(name="Techniques spéciales", value="None ❌", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def top(ctx):
    embed=discord.Embed(title="━━━━━━━━━━━━━━", color=0x3c42fb)
    embed.set_author(name="- CLASSEMENT HEROS -")
    embed.add_field(name="#1: Big Sun", value="90923 pts", inline=False)
    embed.add_field(name="#2: Moonight", value="86849 pts", inline=False)
    embed.add_field(name="#3: Fire Tornado", value="71463 pts", inline=False)
    embed.add_field(name="#4: Dark Light", value="66458 pts", inline=False)
    embed.add_field(name="#5: The Bright", value="63647 pts", inline=False)
    embed.add_field(name="#6: Teleport Speed", value="44249 pts", inline=False)
    embed.add_field(name="#7: Nod", value="41212 pts", inline=False)
    embed.add_field(name="#8: Silver Fist", value="34575 pts", inline=False)
    embed.add_field(name="#9: Counter", value="26766 pts", inline=False)
    embed.add_field(name="#10: Eveillor", value="13655 pts", inline=False)
    await ctx.send(embed=embed)

a=0
@bot.command()
async def f_Me01(ctx):
    def checkMessage(message):
        return message.author==ctx.message.author and ctx.message.channel==message.channel
    await bot.wait_for("message", check=checkMessage)
    embed=discord.Embed(color=0xfd2626)
    embed.add_field(name="Choisit une action... ", value="💥 Attaque\n🛡️ Défense\n☄️ Sournoi", inline=False)
    message=await ctx.send(embed=embed)
    await message.add_reaction("💥")
    await message.add_reaction("🛡️")
    await message.add_reaction("☄")
    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id==reaction.message.id and(str(reaction.emoji) == "💥" or str(reaction.emoji) == "🛡️" or str(reaction.emoji) == "☄")
    
    reaction, user = await bot.wait_for("reaction_add", check=checkEmoji)
    if reaction.emoji == "💥":
        a=1
        embed=discord.Embed(color=0xfd2626)
        embed.add_field(name="💥💥💥 VS ", value="Attaque    -  ", inline=False)
        await ctx.send(embed=embed)
    elif reaction.emoji == "🛡️":
        a=3
        embed=discord.Embed(color=0xfd2626)
        embed.add_field(name="🛡️🛡️🛡️  VS ", value="Défense -  ", inline=False)
        await ctx.send(embed=embed)
    else:
        a=6
        embed=discord.Embed(color=0xfd2626)
        embed.add_field(name="☄️ ☄️ ☄️  VS ", value="Sournois     -  ", inline=False)
        await ctx.send(embed=embed)


bot.run(getenv('TOKEN'))

