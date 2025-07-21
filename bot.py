import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from dolar_api import obtener_dolar_blue, obtener_dolar_oficial

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intent= discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intent)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command(name="dolar")
async def dolar(ctx):
    valor = obtener_dolar_oficial()
    await ctx.send(valor)

@bot.command(name="dolarB")
async def dolar_blue(ctx):
    valor = obtener_dolar_blue()
    await ctx.send(valor)

bot.run(TOKEN)
