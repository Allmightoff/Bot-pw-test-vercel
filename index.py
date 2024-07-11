import discord
from discord.ext import commands

# Remplacez 'your-token-here' par le token de votre bot
TOKEN = 'MTI2MDYzMjQ4MjU0NjQ1MDQ1Mg.GCvGQc.6--3GRDniR3yulkKaWeW1gxoVVGDP7y3WNYLeA'

# Intents
intents = discord.Intents.default()
intents.messages = True

# Initialisation du bot
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Ignore les messages envoyés par le bot lui-même
    if message.author == bot.user:
        return

    # Répond "hello" lorsque le message est "-hello"
    if message.content == '-hello':
        await message.channel.send('hello')

    await bot.process_commands(message)

bot.run(TOKEN)
