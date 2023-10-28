from secondo import scelta, lista
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
message_contents = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("Salve ( ͡° ͜ʖ ͡°)")

@bot.command()
async def consigli(ctx):
    await ctx.send(scelta(sc=random.choice(lista)))
