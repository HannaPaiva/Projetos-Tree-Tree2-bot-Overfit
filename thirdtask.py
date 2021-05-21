import os
import discord
import asyncio
from discord.ext.commands.errors import MemberNotFound
from discord.ext import commands
import csv
PREFIX = '!'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
from datetime import datetime
from discord.flags import MemberCacheFlags
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ctx
import discord
from discord.ext import tasks
import pandas as pd
from discord.ext.commands import Bot

load_dotenv()
intents = discord.Intents.default()
intents.members = True

GUILD = 'Overfit Testes (Hanna)'


intents = discord.Intents().all()
client = discord.Client(intents=intents)
guild = discord.utils.get(client.guilds, name=GUILD)
@bot.command()
async def members(ctx):
    for guild in client.guilds:
        for member in guild.members:
            print(member)
            
ID_Overfit = 839169152467992576 #server overfit 
ID_salado20 = 839169153092288587

ID_teste = 838746575396274219 # server de testes pessoal
ID_sala = 841977130208460821

now = datetime.now()



TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.pxogH1ju_2XKYjC_mbRj12RZQIw'


def filternames(member):
    
    return discord.User.__name__

def filterOnlyBots(member):
    return member.bot
def filterOnlyOnlineMembers(member):
    return member.status == discord.Status.online


@client.event
async def on_ready():
    
    
    print('Bot ativo')

@client.event
async def on_message(message):
  
 if message.content.startswith('a'):   
      
        membersInServer = message.guild.members
        
        channel = message.channel
        
      
        
        now = datetime.now() 
        botsInServer = list(filter(filterOnlyBots, membersInServer))
        botsInServerCount = len(botsInServer)
        names = []
        namesonline = []
        nomemembros = list(list(filter(filternames, membersInServer)))
        tempo = now.strftime("%d/%m/%Y - %H:%M") 
        onlineMembersInServer = list(filter(filterOnlyOnlineMembers, membersInServer))
        usersInServerCount = message.guild.member_count - botsInServerCount
        
        
        fields = ['nome', ' data e hora', ' canal'] 
        filename = "pres.csv"
      
        for items in onlineMembersInServer:
          for it in range(onlineMembersInServer):
           namesonline.append(items.name)
           mydict =[{'nome': items.name, ' data e hora': tempo, ' canal': message.channel}] 
           
           
           with open(filename, 'w') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = fields) 
       
           writer.writeheader() 
           writer.writerows(mydict) 

         
            
          for item in membersInServer:
           names.append(items.name)
        
        
      
        
        #  for li in range(usersInServerCount):
      
        #  writer = file.writelines('Nomes; Data e hora; Canal\n')
        #  output = f'{namesonline}; {tempo}; {message.channel} \n'
        
        
        msg = discord.Embed(title="Quantidade de membros:", description=usersInServerCount, color=0x00FD00)
        msg.add_field(name="Quantidade de bots:",value=botsInServerCount, inline=False)
        
        
        msg.add_field(name="Membros: \n", value = names, inline=True)
        msg.add_field(name="Membros Online: \n ",value= namesonline, inline= True)
        
        await channel.send(embed=msg)
        await channel.send(file=discord.File('pres.csv'))
       
client.run(TOKEN)
