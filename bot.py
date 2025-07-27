import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from dolar_api import informacion_comandos, obtener_dolar_oficial, obtener_dolar_blue, obtener_dolar_bolsa ,obtener_dolar_CCL, obtener_dolar_tarjeta, obtener_dolar_mayorista, obtener_dolar_cripto, obtener_todos_los_valores, obtener_cotizaciones

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command(name="info")
async def info(ctx):
    comandos = informacion_comandos()
    await ctx.send(comandos)

@bot.command(name="dolarOficial")
async def dolar(ctx):
    valor = obtener_dolar_oficial()
    await ctx.send(valor)

@bot.command(name="dolarBlue")
async def dolar_blue(ctx):
    valor = obtener_dolar_blue()
    await ctx.send(valor)

@bot.command(name="dolarBolsa")
async def dolar_bolsa(ctx):
    valor = obtener_dolar_bolsa()
    await ctx.send(valor)

@bot.command(name="dolarCCL")
async def dolar_ccl(ctx):
    valor = obtener_dolar_CCL()
    await ctx.send(valor)

@bot.command(name="dolarTarjeta")
async def dolar_tarjeta(ctx):   
    valor = obtener_dolar_tarjeta()
    await ctx.send(valor)

@bot.command(name="dolarMayorista")
async def dolar_mayorista(ctx):
    valor = obtener_dolar_mayorista()
    await ctx.send(valor)

@bot.command(name="dolarCripto")
async def dolar_cripto(ctx):
    valor = obtener_dolar_cripto()
    await ctx.send(valor)

@bot.command(name="valores")
async def todos_los_valores(ctx):
    mensaje = obtener_todos_los_valores()
    await ctx.send(mensaje)

@bot.command(name="cotizaciones")
async def cotizaciones(ctx):
    mensaje = obtener_cotizaciones()
    await ctx.send(mensaje)

bot.run(TOKEN) # type: ignore
