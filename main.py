import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            name = attachment.filename 
            url = attachment.url
            await attachment.save(name)
            await ctx.send("Archivo guardado correctamente.")
            
            try:
                class_name = get_class("keras_model.h5", "labels.txt", name)
                if class_name == "Palomas":
                    await ctx.send("Esto es una paloma y las palomas pueden comer tata.......")
                elif class_name == "Gorriones":
                    await ctx.send("Esto es un gorrión y esto comen los gorriones ......")

            except: 
                await ctx.send("No se ha podido hacer la clasificación, recuerda que los formatos permitidos son JPG, PNG y JPEG")

    else:
        await ctx.send("No hay archivos adjuntos")


bot.run("TOKEN")