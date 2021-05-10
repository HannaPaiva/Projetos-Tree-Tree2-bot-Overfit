# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'ODM5MDc3Njg4MDA5NDI0OTI3.YJEZ_g.XyA3FTeDy_4yZ9wUrWiXSd8k-OI'

client = discord.Client()

@client.event
async def on_ready():
    print('Seu bot está conectado!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    resposta = 'Presente!'

    if message.content == 'bot!':
        await message.channel.send(resposta)
client.run(TOKEN)