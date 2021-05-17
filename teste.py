import os

import discord
from discord.ext.commands.converter import MemberConverter
from discord.ext.commands.errors import MemberNotFound
from discord.flags import MemberCacheFlags
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()




TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.pxogH1ju_2XKYjC_mbRj12RZQIw'
def filterOnlyBots(member):
    return member.bot

@client.event
async def on_ready():
    
    
    print('Bot ativo')

@client.event
async def on_message(message):
 if message.content.startswith('a'):    
        membersInServer = message.guild.members
        channel = message.channel
        
        # Filter to the list, returns a list of bot-members
        botsInServer = list(filter(filterOnlyBots, membersInServer))
        
        botsInServerCount = len(botsInServer)
        
        
        # (Total Member count - bot count) = Total user count
        usersInServerCount = message.guild.member_count - botsInServerCount
        msg = discord.Embed(title="Quantidade de membros:", description=usersInServerCount, color=0x00FD00)
        msg.add_field(name="Quantidade de bots:",value=botsInServerCount, inline=False)
        await channel.send(embed=msg)
       
        return MemberConverter.status != 'offline' 
       
        
 sum(member.status!=discord.Status.offline and not member.bot for member in message.guild.members)
 


      







client.run(TOKEN)