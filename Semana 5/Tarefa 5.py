import asyncio
from time import time
import discord
from discord import channel
from discord.ext import commands
from datetime import datetime
import asyncio
import time
from datetime import date, timedelta


## ----------------------------- Time assignments for the reminder method -------------------------------------##

format = '%H:%M'
now = datetime.now() 
time_now = now.strftime(format) 

advance_time = '00:15'
advance = '00:15:00'
start_time = '09:30'

reminder = datetime.strptime(start_time, format) - datetime.strptime(advance_time, format)

print(reminder)

## ----------------------------- Time assignment for the cleanup method--------------------------------------##

strtimecleanup = '06:00'
dailytime_cleanup = datetime.strptime(strtimecleanup, format)



## ------------------------------ Assignments and creation variables of the bot ------------------------------##

GUILD = 'Teste'
TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.tzMctjaToj3ua6itVLRiYlJXnnw'   
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents = intents)
guild = discord.utils.get(bot.guilds, name=GUILD)

intents.members = True
bot.remove_command('help')
channel_id = 838746575396274219



async def AsyncioCleanup():
    ''' 
    *****************************************************************************************************************************************

    Description: 
     This method erases all the messages in all text channels in the guild and it is called when the bot starts.  
     It is also always running as a background process. The cleaning is done from time to time (x to x time // like from 2 to 2 hours)
     
    
    Variables:
     args -> It Stores the message that will be sent when the channel has been cleaned;
     argaud -> It Stores the message to be sent if the channel is called "auditório";
     guild -> It is the guild of the Discord where the bot is;
     count -> It will count the number of messages in each channel;
     channel -> It will store all the channels, one by one;
     interval -> Time chosen to be the interval between the cleaning of the channels
     seconds_interval -> Receives the time in the interval and converts to seconds, to use in the method asyncio.sleep()
    
    *****************************************************************************************************************************************
    '''
    
  
    args = 'Este canal foi limpo.  ' 
    argaud = 'Próxima sessão de aprendizagem por pares: 3ª das 17h30 às 19h00 e 5ª das 18h00 às 19h30'
    guild = discord.utils.get(bot.guilds, name=GUILD)
    count = 0 
    interval = datetime(year= now.year, month= now.month, day=now.day, hour= 2, minute=0, second = 0)
    seconds_interval = ((interval.hour * 3600) + (interval.minute * 60) + interval.second)
    print(interval)
    print(seconds_interval)
    while True:      
      
        await asyncio.sleep(seconds_interval)
        for channel in guild.channels:
            async for _ in channel.history(limit=None):
             count = count + 1
            await channel.purge(limit = count)
            await channel.send(args)
            if channel.name == 'auditório':
               await channel.send(argaud)

        break
    
    

## ----------------------- The Daily_Cleanup method, called in the On_ready event ----------------------- ##     
async def Daily_Cleanup():
    ''' 
    *****************************************************************************************************************************************

    Description: 
     This method erases all the messages in all text channels in the guild and it is called when the bot starts.  
     It is also always running as a background process.
     
    
    Variables:
     args -> It Stores the message that will be sent when the channel has been cleaned;
     argaud -> It Stores the message to be sent if the channel is called "auditório";
     guild -> It is the guild of the Discord where the bot is;
     count -> It will count the number of messages in each channel;
     channel -> It will store all the channels, one by one.
     
    
    *****************************************************************************************************************************************
    '''
    
    args = 'Este canal foi limpo.  ' 
    argaud = 'Próxima sessão de aprendizagem por pares: 3ª das 17h30 às 19h00 e 5ª das 18h00 às 19h30'
    guild = discord.utils.get(bot.guilds, name=GUILD)
    count = 0 
    while True:      
        for channel in guild.channels:
            async for _ in channel.history(limit=None):
             count = count + 1
            await channel.purge(limit = count)
            await channel.send(args)
            if channel.name == 'auditório':
               await channel.send(argaud)

        break
    
    
        
        
## ----------------------------------------------- faq command ---------------------------------------------- ##     
      
@bot.command(name='faq')
async def FAQ(ctx):
    ''' 
    *****************************************************************************************************************************************

    Description: 
     This method allows the member to access the frequently asked questions, by sending a embed message with a hyperlink to a google sites
     (where the questions and answers will be).
     
    Parameters:
     ctx -> variable that receives the command. 
  
    Variables:
     embed -> class embed variable, to send the message with a hyperlink
    
     
    
    *****************************************************************************************************************************************
    '''
   
    embed = discord.Embed()
    embed.description = "Você pode aceder ao FAQ do Overfit [aqui](https://sites.google.com/aeffl.pt/faq-overfit/p%C3%A1gina-inicial?authuser=1)."
    await ctx.send(embed=embed)
  



## ----------------------- The reminder method, called in the On_ready event ----------------------- ##     
async def Reminder():
    ''' 
    *****************************************************************************************************************************************

    Description: 
     This method is called when the bot starts, and it is always running as a background process.
     Its purpose is to send messages to the private chat of the guild members with a specific role. 
     In this case, when the time is the same as the one assigned to the 'reminder',
     it sends a message to all students with the given rolename, attached to a timer that shows how much time is left for the session.
    
    Variables:
     now -> Datetime variable that is always verifying the time;
     reminder -> It is the time that the the message will be sent at; 
     guild -> The guild;
     role -> The role of the members that will be sorted by the name of the role;
     number-> It retains the time in "advance", that is in string, converted in Datetime;
     seconds-> It retains the time in "number", converting all the given time in seconds;
     h -> It is the form of output of the time. It gets the seconds and transforms it in H:M:S;
     msg -> the message with the timer to be sent and edited.
    
    *****************************************************************************************************************************************
    '''
    while True:
        
        now = datetime.now().strftime(format) 
        
        if  now == reminder:
            
            role_name = 'aluno'
            guild = discord.utils.get(bot.guilds, name=GUILD)
            role = discord.utils.find(lambda r: r.name == role_name, guild.roles)
            members = guild.members
            
            #"number" retains the time in "advance", that is in string, converted in Datetime
            number = datetime.strptime(advance, '%H:%M:%S')
            
            #"seconds" retains the time in "number", converting all time in seconds
            seconds = (number.hour * 3600) + (number.minute * 60) + number.second

            #h is the form of output of the hour. It gets the seconds and transforms in H:M:S
            h = time.strftime('%H:%M:%S', time.gmtime(seconds))
            
            
            args = f"Olá!! Estou aqui para avisar que nossas atividades começarão logo!!"  
            
            for member in members:
                    msg = None
                    if role in member.roles:

                        await member.send(args)
                        msg = await member.send("Tempo restante: ")
                    
                        while seconds != 0:
                            
                            h = time.strftime('%H:%M:%S', time.gmtime(seconds))
                            seconds -= 1
                            
                            await msg.edit(content= f'Tempo restante: {h}')
                            await asyncio.sleep(1)
                            
                        await msg.edit(content='Fim!')
        break

## ----------------------- on_ready, that calls the methods when the bot is ready to be used ----------------------- ##

@bot.event
async def on_ready():
    ''' 
    *****************************************************************************************************************************************
    
    Description: 
     The on_ready method is the method that runs when the bot is ready to be used/connected.
    
    *****************************************************************************************************************************************
    '''
    print(f'{bot.user.name} está conectado!')
   # await Daily_Cleanup()
    await AsyncioCleanup()
    await Reminder()
    
## ---------------- Help Command, that shows all the commands available in the bot ----------------------- ##        
@bot.command(name='help')
async def help(ctx):
    ''' 
    *****************************************************************************************************************************************

    Description: 
     When the command "help" is inserted in the channel, it shows all the commands available in the bot. The commands are kept in a .txt file.
    
    Parameters:
     ctx -> variable that receives the command.
    
    Variables:
     fmr -> It is an array used to make the output of the file appears line by line;
     msg -> It is a variable used to send the message in the channel.
    
    *****************************************************************************************************************************************
    '''
    
    fmr = []
 
    with open ('help.txt', 'r', encoding='utf-8') as file:
       hlp = file.readlines() 
       
       fmr = "\n".join(hlp)

   
    msg = discord.Embed(title=f"Comandos que {bot.user.name} possui: ", description= '', color=0xDC143C)
        
    msg.add_field(name= '**', value = fmr, inline = False)

    await ctx.channel.send(embed=msg)
    
## ----------------------- method that counts an inserted time ----------------------- ##
@bot.command(name='t') 
async def InputTimer(ctx, number:int):
 ''' 
  *****************************************************************************************************************************************
  
  Description: 
   This method basically receives the command with an input of a number, which is the number of seconds, and it counts the time by sending a 
   message and editing the same message in a loop, decreasing the number of seconds 1 by 1.
 
  Parameters:
   ctx -> variable that receives the command;
   number-> variable that stores the seconds to be counted.
 
  Variables:
   h -> is the converter from time in seconds to the given time format;
   The function counts -1 every 1 second;
   message -> saves the message to be sent, so it can be edited in the loop.
  
  *****************************************************************************************************************************************
 '''
 
 try:
  if number < 0:
        await ctx.send('O tempo não pode ser negativo')
  else:
        h = time.strftime('%H:%M:%S', time.gmtime(number))
        message = await ctx.send(h)
        
        while number != 0:
            number -= 1
            h = time.strftime('%H:%M:%S', time.gmtime(number))
            await message.edit(content=h)
            await asyncio.sleep(1)
            
        await message.edit(content='Fim!')

 except ValueError:
     
        await ctx.send(' O tempo precisa ser um número...')
        
        
## ----------------------- timer that counts an already given time ----------------------- ##        
@bot.command(name='timer')
async def Timer_1hour(ctx):
 ''' 
 *****************************************************************************************************************************************
 
 Description: 
  This method counts the time in the exact same way as the "InputTimer", by sending and editing the message. 
 
 Parameters:
  ctx -> variable that receives the command. 
    
 Variables:
   now -> keeps the current time, which is the start of the timer count;
   ctime -> convert now to the time format;
   number-> time, in seconds, preset = 1 hour;
   h -> is the converter from time in seconds to time format;
   message -> saves the message to be sent, so it can be edited later.
 
*****************************************************************************************************************************************
 '''
 
 now = datetime.now() 
 ctime = now.strftime("%H:%M:%S") 
 number = 3600
 message = await ctx.send(f"Hora de início: {ctime}")
 message = await ctx.send(number)

 while number != 0:
    h = time.strftime('%H:%M:%S', time.gmtime(number))
    number -= 1
    await message.edit(content= h)
    await asyncio.sleep(1)
 await message.edit(content='Fim!')


## ----------------------- método que limpa as mensagens ----------------------- ##    

@bot.command(name='cls')
@commands.has_any_role('admin')
async def count(ctx):
    '''
    *****************************************************************************************************************************************
    
    Description: 
     This method deletes all the messages in the history of the channel
    
    Parameters:
     ctx -> variable that receives the command. 
        
    Variables:
     channel -> stores the channel where the message was sent
     count - > stores the amount of messages in the channel to delete the messages
    
    *****************************************************************************************************************************************
    '''


    channel = ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count = count + 1
        await ctx.channel.purge(limit = count)
  
       
## ---------------- método que devolve a quantidade de mensagens de um canal de texto ----------------------- ##        
@bot.command(name = 'contar_mensagens')
@commands.has_any_role('admin')
async def message_count(ctx, channel: discord.TextChannel=None):
    ''' 
    *****************************************************************************************************************************************
    
    Description: 
     This method counts all the messages in the history of the channel
    
    Parameters:
     ctx -> variable that receives the command. 
        
    Variables:
     channel -> stores the channel where the message was sent
     count - > stores the amount of messages in the channel to be counted
    
    
    *****************************************************************************************************************************************
    '''
    
    
    channel = ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("Há {} mensagens no canal {}".format(count, channel.mention))
    
    
    
## ---------------- método que envia saudações no privado do autor da mensagem ----------------------- ##        

@bot.command(name='greet')
async def msgprivada(ctx):
    '''
    *****************************************************************************************************************************************
    
    Description: 
     When the command "!greet" is inserted in the channel, this method sends a greeting message
     to the private chat to the member who sent the message
    
    Parameters:
     ctx -> variable that receives the command. 
    
    *****************************************************************************************************************************************
    '''
    
    await ctx.author.send("Olá!! :D")
    

## ---------------- método que envia uma mensagem inserida para um membro específico ----------------------- ##       
@bot.command(name='dm')
@commands.has_any_role('admin')
async def dm(ctx, user_id = None, *, args = None):
 '''
    *****************************************************************************************************************************************
  
    Description: 
     When the command "!dm (+ message you want to be sent)" is inserted, it sends a message to the private channel of the member with a certain ID
    
    Parameters:
     ctx -> variable that receives the command; 
     user_id -> the user ID that will be inserted;
     args -> the message to be sent.
    
    Variables:
     target -> this one will fetch the user with the ID that will be given.
    
    *****************************************************************************************************************************************
 '''
 
 
 if user_id != None and args != None:
     try:
         target = await bot.fetch_user(user_id)
         await target.send(args)
         await ctx.channel.send("'" + args + "'" + " Foi enviada para: " + target.name )
     except:
        await ctx.channel.send("Não foi possível mandar a mensager")
        
        

## ---------------- método que envia uma mensagem inserida para todos os membros ----------------------- ##       
@bot.command(name='alldm')
@commands.has_any_role('admin')
async def alldm(ctx, *, args = None):
  '''
    *****************************************************************************************************************************************
    
    Description: 
     When the command "!alldm(+ message you want to be sent)" is inserted, it sends a message to the private channel of all members in the server
      
    Parameters:
     ctx -> variable that receives the command; 
     args -> the message to be sent.
    
    Variables:
     member & members -> these will run through all of the members in the guild
     
    *****************************************************************************************************************************************
 '''
  
  if args != None:
     members = ctx.guild.members
     for member in members:
        if member != bot.user.name:
         try:
          await member.send(args)
          await ctx.channel.send("'" + args + "'" + " Foi enviada para: " + member.name)
         except:
          print("Não foi possível enviar '" + args + "' para" + member.name)
  else: 
         await ctx.channel.send ("faltaram argumentos")
        
## ---------------- método que devolve todos os membros com a role "admin" ----------------------- ##      
@bot.command(name = 'gtmin')
@commands.has_any_role('admin')
async def get_admins(ctx):
    '''
    *****************************************************************************************************************************************
    
    Description: 
     When the command "!gtmin" is inserted in the channel, it returns all the members with the "admin" role.
    
    Parameters:
     ctx -> variable that receives the command; 
    
    Variables:
     role_name -> it is the name of a specific role of the guild
     role -> this one will search/find that role with the given name
     user -> this will run through the members
    
    *****************************************************************************************************************************************
    
    
    '''  
    
    role_name = 'admin'
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
        
    for user in ctx.guild.members:
        if role in user.roles:
            await ctx.send(f"**{user.name}** possui o cargo: '{role}'")
            
            
            
            
## ---------------- método que devolve todos os membros com a role "aluno" ----------------------- ##                 
@bot.command(name = 'gtaluno')
@commands.has_any_role('admin')
async def get_alunos(ctx):
    '''
    *****************************************************************************************************************************************
    
    Description: 
     When the command "!gtaluno" is inserted in the channel, it returns all the members with the "admin" role.
    
    Parameters:
     ctx -> variable that receives the command; 
    
    Variables:
     role_name -> it is the name of a specific role of the guild;
     role -> this one will search/find that role with the given name;
     user -> this will run through the members.
     
    *****************************************************************************************************************************************
    
    '''  
    role_name = 'aluno'
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
        
    for user in ctx.guild.members:
        if role in user.roles:
            await ctx.send(f"**{user.name}** possui o cargo: '{role}'")
  
## ----------------------- método que envia mensagem a todos os alunos ----------------------- ##           
@bot.command(name = 'msaluno')
@commands.has_any_role('admin')
async def msalunos(ctx):
   '''
    *****************************************************************************************************************************************
    
    Description: 
     It sends a message to all members with the "aluno" role // "args" is the message to be sent. 
    
    Parameters:
     ctx -> variable that receives the command; 
    
    Variables:
     role_name -> it is the name of a specific role of the guild
     role -> this one will search/find that role with the given name
     user -> this will run through the members
    
    *****************************************************************************************************************************************
    '''
    

   
   args = "Você possui o cargo de Aluno :D"
   role_name = 'aluno'
   role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
   members = ctx.guild.members
   
   for member in members:
        if role in member.roles:
            await member.send(args)
   
            
## ----------------------- método que envia mensagem a todos os administradores ----------------------- ##              
@bot.command(name = 'msadmin')
@commands.has_any_role('admin')
async def msalunos(ctx):
 '''
    *****************************************************************************************************************************************
    
    Description: 
     It sends a message to all members with the "admin" role // "args" is the message to be sent. '''   
 
 args = "Você possui o cargo de admin :D"
 role_name = 'admin'
 role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
 members = ctx.guild.members
   
 for member in members:
    if role in member.roles:
        await member.send(args)
        
        

    
        
            
    
bot.run(TOKEN) 
