import discord
from discord.ext import commands

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '-hello':
        await message.channel.send('hello')
    await bot.process_commands(message)

bot.run(TOKEN)
