import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from dolar_api import informacion_comandos, obtener_dolar_blue, obtener_dolar_oficial, obtener_todos_los_valores

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # <- ¡MUY IMPORTANTE!
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command(name="info")
async def info(ctx):
    comandos = informacion_comandos()
    await ctx.send(comandos)

@bot.command(name="dolar")
async def dolar(ctx):
    valor = obtener_dolar_oficial()
    await ctx.send(valor)

@bot.command(name="dolarB")
async def dolar_blue(ctx):
    valor = obtener_dolar_blue()
    await ctx.send(valor)

@bot.command(name="valores")
async def todos_los_valores(ctx):
    mensaje = obtener_todos_los_valores()
    await ctx.send(mensaje)

bot.run(TOKEN)
