import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='ZT!', description="Esto es un bot de ZeroTwo")

@bot.command()
async def ayuda(ctx):
    await ctx.send('Darling, utiliza los siguientes comandos para ejecutar acciones:' + 
                    '\n' + '**ZT!Ayuda**: Comando para obtener la lista de comandos que acepta ZeroTwo.' +
                    '\n' + '**ZT!Eat**: Comando para darme de comer una hamburguesa, ñom!' + 
                    '\n' + '**ZT!ZeroTwo**: ¡Darling!' + 
                    '\n' + '**ZT!Smile**: Comando para hacerme sonreir.' + 
                    '\n' + '**ZT!Ahh**: Comando para que te dé de comer, Darling.')

@bot.command()
async def eat(ctx):
    await ctx.send('https://tenor.com/view/zero-two-burger-zero-two-002-dit-f-anime-burger-gif-15429963')

@bot.command()
async def ZeroTwo(ctx):
    await ctx.send("¡Darling!")

@bot.command()
async def Smile(ctx):
    await ctx.send('https://tenor.com/view/zero-two-002-cute-anime-wink-gif-11994868')

@bot.command()
async def Ahh(ctx):
    await ctx.send('https://tenor.com/view/zero-two-gif-20649457')

@bot.command()
async def confuse(ctx):
    await ctx.send('https://tenor.com/view/zero-two-blink-anime-gif-14226163')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"Zero Two", description="Hola! Soy 002, mejor conocida cómo Zero Two"
    , color=discord.Color.from_rgb(237, 207, 207))
    embed.set_thumbnail(url='https://p4.wallpaperbetter.com/wallpaper/147/282/530/anime-darling-in-the-franxx-pink-hair-smile-zero-two-darling-in-the-franxx-hd-wallpaper-preview.jpg')
    embed.add_field(name ="Acerca de mí", value="Soy la mejor piloto, mi FRANXX es Strelizia", inline=True)
    embed.set_image(url='https://c.wallhere.com/photos/1e/26/anime_anime_girls_darling_in_franxx_Darling_in_the_FranXX_Zero_Two_Zero_Two_Darling_in_the_FranXX-1316631.jpg!d')
    
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DARLING in the FRANXX, en espera de una segunda temporada"))
    print('Lista, darling')

bot.run('ODI2NTc0OTQxNjIwOTI4NTEz.YGOd5w.2gjcaFVuIvO52F9evH-RnRKV8WM')