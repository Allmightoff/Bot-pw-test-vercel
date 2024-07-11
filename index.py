import discord
from discord.ext import commands
import os

# Utilise le token du bot depuis les variables d'environnement
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Intents
intents = discord.Intents.default()
intents.message_content = True  # Assurez-vous que ceci est correctement configuré

# Initialisation du bot
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    print(f"Received message: {message.content} from {message.author}")
    
    # Ignore les messages envoyés par le bot lui-même
    if message.author == bot.user:
        return

    # Répond "hello" lorsque le message est "-hello"
    if message.content == '-hello':
        await message.channel.send('hello')

    await bot.process_commands(message)

bot.run(TOKEN)
