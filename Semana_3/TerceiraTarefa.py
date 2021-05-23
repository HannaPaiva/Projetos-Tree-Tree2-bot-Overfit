import os
import discord
import asyncio
from discord.ext import commands
import csv
from datetime import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ctx
import discord
from discord.ext.commands import Bot

PREFIX = '!'

load_dotenv()

GUILD = 'Overfit Testes (Hanna)'

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
guild = discord.utils.get(client.guilds, name=GUILD)


# @bot.command()
# async def members(ctx):
#     for guild in client.guilds:
#         for member in guild.members:
#             print(member)
            
TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.pxogH1ju_2XKYjC_mbRj12RZQIw'   
ID_Overfit = 839169152467992576 #server overfit 
ID_salado20 = 839169153092288587

ID_teste = 838746575396274219 # server de testes pessoal
ID_sala = 841977130208460821

now = datetime.now()

def filternames(member):
    return member.name

def filterOnlyBots(member):
    return member.bot

def filterOnlyOnlineMembers(member):
    return member.status != discord.Status.offline


@client.event
async def on_ready():
    
    print('Bot ativo')


@client.event
async def on_message(message):
    
 for guild in client.guilds:
        for member in guild.members:
            membros = member
            
        membersInServer = message.guild.members
        
        channel = message.channel
        
      
        
        now = datetime.now() 
        botsInServer = list(filter(filterOnlyBots, membersInServer))
        botsInServerCount = len(botsInServer)
        names = []
        namesonline = []
        nomemembros = list(list(filter(filternames, membersInServer)))
        tempo = now.strftime("%d/%m/%Y - %H:%M") 
        data = now.strftime("%d/%m/%Y") 
        onlineMembersInServer = list(filter(filterOnlyOnlineMembers, membersInServer))
        usersInServerCount = message.guild.member_count - botsInServerCount
        
 if message.content == "!presenças":   
      
        
        with open ('pres.csv', 'w', newline = '') as file:
            write = file.write('Nome; Data e Hora; canal \n')
            writer = csv.writer(file, delimiter = ';')
            for membros in guild.members:
                writer = csv.writer(file, delimiter = '"')
                
                if membros.status != discord.Status.offline:
                    writer.writerow([membros.name + '; ' + tempo + '; ' + str(channel.name)])
   
      
        await channel.send(f'Presenças da data: {data} ')
        await channel.send(file=discord.File('pres.csv'))
        
 elif message.content == "!status":   
     
        for items in onlineMembersInServer:
           namesonline.append(items.name)
           online = "; \n".join(namesonline) + '.'
           
        for item in membersInServer:
           names.append(item.name)
           nomes = "; \n".join(names) + '.'
             
        msg = discord.Embed(title=f"Presentes a {tempo}", description= '', color=0xDC143C)
        
        msg.add_field(name="Quantidade de membros:", value =usersInServerCount, inline = False)
        msg.add_field(name="Quantidade de bots:",value=botsInServerCount, inline=False)
        
        
        msg.add_field(name="Membros: \n", value = nomes, inline=True)
        msg.add_field(name="Membros Online: \n ",value= online, inline= True)
        
        await channel.send(embed=msg)
      
       
client.run(TOKEN)
