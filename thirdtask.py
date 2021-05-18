import os
import discord
import asyncio
from discord.ext.commands.converter import MemberConverter
from discord.ext.commands.errors import MemberNotFound
from discord.ext import commands

PREFIX = '!'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)

from discord.flags import MemberCacheFlags
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ctx

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
GUILD = 'Overfit Testes (Hanna)'
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


TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.pxogH1ju_2XKYjC_mbRj12RZQIw'

def filternames(member):
    return member.name

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
      
        botsInServer = list(filter(filterOnlyBots, membersInServer))
        botsInServerCount = len(botsInServer)
        
        nomemembros = list(list(filter(filternames, membersInServer)))
        onlineMembersInServer = list(filter(filterOnlyOnlineMembers, membersInServer))
        usersInServerCount = message.guild.member_count - botsInServerCount
        
        
        msg = discord.Embed(title="Quantidade de membros:", description=usersInServerCount, color=0x00FD00)
        msg.add_field(name="Quantidade de bots:",value=botsInServerCount, inline=False)
        msg.add_field(name="Membros:", value = nomemembros, inline=True)
        msg.add_field(name="Membros Online: ",value= onlineMembersInServer, inline= True)
        await channel.send(embed=msg)
        print(member.status!=discord.Status.offline for member in message.guild.members)
        

client.run(TOKEN)
