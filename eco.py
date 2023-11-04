from secondo import scelta, lista
import discord
import random
from discord.ext import commands
import time

intents = discord.Intents.default()
message_contents = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("Salve ( ͡° ͜ʖ ͡°)")

@bot.command()
async def consigli(ctx):
    consiglio_scelto = random.choice(lista)
    await ctx.send(f"Ecco a te un consiglio sull'inquinamento:\n{consiglio_scelto}")
        
        



        

