# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.pxogH1ju_2XKYjC_mbRj12RZQIw'
GUILD = 'Overfit Testes (Hanna)'

ID_Overfit = 839169152467992576 #server overfit 
ID_salado20 = 839169153092288587

ID_teste = 838746575396274219 # server de testes pessoal
ID_sala = 841977130208460821

client = discord.Client()

@client.event
async def on_ready():
    
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    contador = guild.memberCount
    members = '\n - '.join([member.name for member in guild.members])
    op = members
    print(f'Membros ativos:\n - {members}')


@client.event
async def on_message(message):
  
    id = client.get_guild(ID_Overfit)
    
    channels = ["sala-do-20"]
    
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    print(
        f'{client.user} is connected to the following guild:\n')
     
   
    membros = '\n - '.join([member.name for member in guild.members])
   
    print(f'Membros ativos:\n - {membros}')

    if str(message.channel) in channels:  
        if client.user != message.author :
            
         if message.content == "a":
          await message.channel.send(f'Sou a {client.user.name}, com a ID {client.user.id}, e no canal {message.channel}')
          
          await message.channel.send(f'Membros ativos: \n - {membros} ')
          
client.run(TOKEN)