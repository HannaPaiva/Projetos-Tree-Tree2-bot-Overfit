import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import time
import pytz
import csv
import discord.utils
from dotenv import load_dotenv
import os
load_dotenv('.env')

timezone = datetime.now(pytz.timezone('Europe/Lisbon'))

## ----------------------------- Time assignments for the reminder method -------------------------------------##

format = '%H:%M'
now = datetime.now(pytz.timezone('Europe/Lisbon'))
time_now = now.strftime(format)

advance_time = '00:15'
advance = '00:15:00'
start_time = '09:00'

reminder = datetime.strptime(start_time, format) - datetime.strptime(advance_time, format)
print(f"Agora são {now}")
print(f"Tempo do lembrete diário = {reminder}")


## ------------------------------ Assignments and creation variables of the bot ------------------------------##

GUILD = 'Overfit Testes (Hanna)'
TOKEN = os.getenv('TOKEN')
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
guild = discord.utils.get(bot.guilds, name=GUILD)

intents.members = True
bot.remove_command('help') # you have to remove it so you can write your own.

## ----------------------------- Time assignment for the daily cleanup method--------------------------------------##

strtimecleanup = '08:00'
dailytime_cleanup = datetime.strptime(strtimecleanup, format)

print(f'Limpeza diária = {strtimecleanup}')


async def AsyncioCleanup():
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     This method erases all the messages in all text channels in the guild and it is called when the bot starts.  
     It is also always running as a background process. The cleaning is done from time to time (x to x time // like from 2 to 2 hours)


    ###  Variables:
     args -> It Stores the message that will be sent when the channel has been cleaned;
     argaud -> It Stores the message to be sent if the channel is called "auditório";
     guild -> It is the guild of the Discord where the bot is;
     count -> It will count the number of messages in each channel;
     channel -> It will store all the channels, one by one;
     interval -> Time chosen to be the interval between the cleaning of the channels;
     seconds_interval -> Receives the time in the interval and converts to seconds, to use in the method asyncio.sleep().

    *****************************************************************************************************************************************
    '''

    args = 'Este canal foi limpo.'
    argaud = 'Próxima sessão de aprendizagem por pares: 3ª das 17h30 às 19h00 e 5ª das 18h00 às 19h30'
    guild = discord.utils.get(bot.guilds, name=GUILD)
    channel = discord.utils.get
    count = 0
    interval = datetime(year=now.year, month=now.month,
                        day=now.day, hour=2, minute=0, second=00)
    seconds_interval = ((interval.hour * 3600) +
                        (interval.minute * 60) + interval.second)
    print(f"Espaço de tempo para a limpeza = {interval.strftime('%H:%M:%S')}")

    while True:

        await asyncio.sleep(seconds_interval)
        for guild in bot.guilds:
          for channel in guild.text_channels:
                count = count + 1

                await channel.purge(limit=count)

                await channel.send(args)
                if channel.name == 'auditório':

                    await channel.send(argaud)

     


## ----------------------- The Daily_Cleanup method, called in the On_ready event ----------------------- ##
async def Daily_Cleanup():
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     This method erases all the messages every day in a given time, in all text channels in the guild, and it 
     is called when the bot starts. It is also always running as a background process.


    ### Variables:
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
        now = datetime.now(pytz.timezone('Europe/Lisbon')).strftime(format)

        if now == strtimecleanup:

            for channel in guild.text_channels:
                async for _ in channel.history(limit=None):
                    count = count + 1
                await channel.purge(limit=count)
                await channel.send(args)
                if channel.name == 'auditório':
                    await channel.send(argaud)

        break


## ----------------------------------------------- faq command ---------------------------------------------- ##

@bot.command(name='faq')
async def FAQ(ctx):
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     This method allows the member to access the frequently asked questions, by sending a embed message with a hyperlink to a google sites
     (where the questions and answers will be).

    ### Parameters:
     ctx -> Variable that receives the command. 

    ### Variables:
     embed -> Class embed variable, to send the message with a hyperlink

    *****************************************************************************************************************************************
    '''

    embed = discord.Embed()
    embed.description = "Você pode aceder ao FAQ do Overfit [aqui](https://sites.google.com/aeffl.pt/faq-overfit/p%C3%A1gina-inicial?authuser=1)."
    await ctx.send(embed=embed)


## ----------------------- The reminder method, called in the On_ready event ----------------------- ##
async def Reminder():
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     This method is called when the bot starts, and it is always running as a background process.
     Its purpose is to send messages to the private chat of the guild members with a specific role. 
     In this case, when the time is the same as the one assigned to the 'reminder' variable,
     it sends a message to all students with the given role name, attached to a timer that shows how much time is left for the session.

    ### Variables:
     now -> Datetime variable that is always verifying the time;
     reminder -> It is the time that the the message will be sent at; 
     guild -> The guild;
     role -> The role of the members that will be sorted by the name of the role;
     number-> It retains the time in "advance", that is in string, converted in Datetime;
     seconds-> It retains the time in "number", converting all the given time in seconds;
     h -> It is the form of output of the time. It gets the seconds and transforms it in H:M:S;
     msg -> The message with the timer to be sent and edited.

    *****************************************************************************************************************************************
    '''
    while True:

        now = datetime.now(pytz.timezone('Europe/Lisbon')).strftime(format)

        if now == reminder:

            role_name = 'aluno'
            guild = discord.utils.get(bot.guilds, name=GUILD)
            role = discord.utils.find(
                lambda r: r.name == role_name, guild.roles)
            members = guild.members

            # "number" retains the time in "advance", that is in string, converted in Datetime
            number = datetime.strptime(advance, '%H:%M:%S')

            # "seconds" retains the time in "number", converting all time in seconds
            seconds = (number.hour * 3600) + \
                (number.minute * 60) + number.second

            # h is the form of output of the hour. It gets the seconds and transforms in H:M:S
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

                        await msg.edit(content=f'Tempo restante: {h}')
                        await asyncio.sleep(1)

                    await msg.edit(content='Fim!')
               



@bot.event
async def on_member_join(member):
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     This method is called when the member enters a server, and it sends a welcome message to the member 
     in the 'channel of greetings', alongside with the profile picture of the member. 
    *****************************************************************************************************************************************
     '''
    ID_Welcome_channel = 855023194586742784
    channel = bot.get_channel(ID_Welcome_channel)
    embed=discord.Embed(title=f"Seja bem-vindo ao servidor do Overfit, {member.name}!!", description=f" {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!

    await channel.send(embed=embed)
   

## ----------------------- on_ready, that calls the methods when the bot is ready to be used ----------------------- ##
@bot.event
async def on_ready():
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     The on_ready method is the method that runs when the bot is ready to be used/connected.
     it is calling the AsyncioCleanup() method, the Daily Cleanup method, and the Reminder() method;

    *****************************************************************************************************************************************
    '''
    print(f'{bot.user.name} está conectado!')
    await Daily_Cleanup()
    await AsyncioCleanup()
    await Reminder()


## ------------------------------------ ##

@bot.command(name='delete')
@commands.has_any_role('admin')
async def cleanupv2(ctx, channel_name):
    '''
     *****************************************************************************************************************************************

     ### Description: 
      This method deletes a text channel when the command "!delete <name of the text channel> is given. If the channel doesn't exist
      it sends a message saying that it doesn't. 

     ### Parameters:
      ctx -> Variable that receives the command;
      channel_name -> The name of the channel to be inserted.

     ### Variables:

      guild -> Current guild;
      existing_channel -> run through the channels and get the channel with the given name. 

     *****************************************************************************************************************************************
    '''
    guild = ctx.message.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    if existing_channel is not None:
        await existing_channel.delete()
        
    elif existing_channel is None:
        await ctx.channel.send("O canal não existe")


@bot.command(name='defcreate')
async def create(ctx, channel_name):
    '''
     *****************************************************************************************************************************************

     ### Description: 
      This method creates a text channel in the top of the channels when the command "!defcreate <name of the text channel> is given.
      If the channel already exists, it sends a message saying that it does. 

     ### Parameters:
      ctx -> Variable that receives the command;
      channel_name -> The name of the channel to be inserted.

     ### Variables:

      guild -> Current guild;
      existing_channel -> run through the channels and get the channel with the given name. 


     *****************************************************************************************************************************************
    '''

    guild = ctx.message.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    if existing_channel is None:
        await guild.create_text_channel(channel_name, type=discord.ChannelType.text)


@bot.command(name='create')
@commands.has_any_role('admin')
async def create(ctx, channel_name, categ):
    '''
     *****************************************************************************************************************************************

     ### Description: 
      This method creates a text channel when the command "!create <name of the text channel> <category> is given.
      If the channel already exists, it sends a message saying that it already does. 

     ### Parameters:
      ctx -> Variable that receives the command;
      channel_name -> The name of the channel to be inserted;
      categ -> The name of the category.

     ### Variables:
      guild -> Current guild;
      existing_channel -> run through the channels and get the channel with the given name. 

     *****************************************************************************************************************************************
     '''
    guild = ctx.message.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    category = discord.utils.get(guild.categories, name=categ)

    if existing_channel is None and category is not None:
        await guild.create_text_channel(channel_name, type=discord.ChannelType.text, category=category)
        
    else:
        
     if existing_channel is not None:
        await ctx.channel.send("Este canal já existe!")

     if category is None:
        await ctx.channel.send("Essa categoria não existe :c")


@bot.command(name='categ')
@commands.has_any_role('admin')
async def category(ctx, category_name):
    '''
     *****************************************************************************************************************************************

     ### Description: 
      This method creates a category when the command "!categ <name of the category> is given.


     ### Parameters:
      ctx -> Variable that receives the command;
      category_name -> The name of the category.

     ### Variables:

      guild -> Current guild;
      category -> search in the guild categories, and get the one that has the given name;

     *****************************************************************************************************************************************
     '''
    guild = ctx.message.guild

    category = discord.utils.get(guild.categories, name=category_name)
    if category is None:
        await guild.create_category(category_name)


@bot.command(name='help')
async def help(ctx):
    ''' 
    *****************************************************************************************************************************************

     ### Description: 
     When the command "help" is inserted in the channel, it shows all the commands available in the bot. The commands are kept in a .txt file.

     ### Parameters:
     ctx -> Variable that receives the command.

     ### Variables:
     fmr -> It is an array used to make the output of the file appears line by line;
     msg -> It is a variable used to send the message in the channel.

    *****************************************************************************************************************************************
    '''

    fmr = []

    with open('help.txt', 'r', encoding='utf-8') as file:
        hlp = file.readlines()

        fmr = "\n".join(hlp)

    msg = discord.Embed(
        title=f"Comandos que {bot.user.name} possui: ", description='', color=0xDC143C)

    msg.add_field(name='**', value=fmr, inline=False)

    await ctx.channel.send(embed=msg)

## ------------------------------------ ##


@bot.command(name='t')
async def InputTimer(ctx, number: int):
    ''' 
     *****************************************************************************************************************************************

     ### Description: 
       This method receives the command with an input of a number, which is the number of seconds you want to be counted, and 
       it counts the time by sending a message and editing the same message in a loop, decreasing the number of seconds 1 by 1.

     ### Parameters:
       ctx -> Variable that receives the command;
       number-> Variable that stores the seconds to be counted.

     ### Variables:
      h -> Is the converter from time in seconds to the given time format; 
      number -> The seconds to be converted to the right format with "h";
      message -> It saves the message to be sent, so it can be edited in the loop.

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


## ------------------------------------ ##
@bot.command(name='timer')
async def Timer_1hour(ctx):
    ''' 
    *****************************************************************************************************************************************

        ### Description: 
           This method counts the time by sending a message and editing the same message in a loop, decreasing the number of seconds 1 by 1. 
           The default number of seconds is 3600, which is one hour. It will count 1 hour by default.

        ### Parameters:
           ctx -> Variable that receives the command. 

        ### Variables:
           now -> Keeps the current time, which is the start of the timer count;
           ctime -> Converts "now" to the time defined format;
           number-> Time, in seconds; default = 1 hour;
           h -> Is the converter from time in seconds to time format;
           message -> It saves the message to be sent, so it can be edited later. 

   *****************************************************************************************************************************************
    '''

    number = 3600
    while number != 0:
        h = time.strftime('%H:%M:%S', time.gmtime(number))
        message = await ctx.send(h)

        while number != 0:
            number -= 1
            h = time.strftime('%H:%M:%S', time.gmtime(number))
            await message.edit(content=h)
            await asyncio.sleep(1)

        await message.edit(content='Fim!')


## ------------------------------------ ##

@bot.command(name='cls')
@commands.has_any_role('admin')
async def cls(ctx):
    '''
    *****************************************************************************************************************************************

     ### Description: 
     This method deletes all the messages in the history of the channel where the message was sent.

     ### Parameters:
     ctx -> Variable that receives the command. 

     ### Variables:
     channel -> Stores the channel where the message was sent
     count - > Stores the amount of messages in the channel to delete the messages

    *****************************************************************************************************************************************
    '''

    channel = ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count = count + 1
        await ctx.channel.purge(limit=count)


## ------------------------------------ ##
@bot.command(name='contar_mensagens')
@commands.has_any_role('admin')
async def message_count(ctx, channel: discord.TextChannel = None):
    ''' 
    *****************************************************************************************************************************************

     ### Description: 
     This method counts and returns the amount of messages in the channel where the message was sent.

     ### Parameters:
     ctx -> Variable that receives the command. 

     ### Variables:
     channel -> Stores the channel where the message was sent;
     count - > Stores the amount of messages in the channel to be counted.

    *****************************************************************************************************************************************
    '''

    channel = ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("Há {} mensagens no canal {}".format(count, channel.mention))


## ------------------------------------ ##

@bot.command(name='greet')
async def msgprivada(ctx):
    '''
    *****************************************************************************************************************************************

     ### Description: 
     When the command "!greet" is inserted in the channel, this method sends a greeting message
     to the private chat to the member who sent the message in the first place. 

     ### Parameters:
     ctx -> Variable that receives the command. 

    *****************************************************************************************************************************************
    '''

    await ctx.author.send("Olá!! :D")


## --------------------------------------- ##
@bot.command(name='dm')
@commands.has_any_role('admin')
async def dm(ctx, user_id=None, *, args=None):
    '''
       *****************************************************************************************************************************************

        ### Description: 
        When the command "!dm (+ message you want to be sent)" is inserted, it sends the inserted message to the private channel
        of the member with a certain ID.

        ### Parameters:
        ctx -> Variable that receives the command; 
        user_id -> The user ID that will be inserted;
        args -> The message to be sent.

        ### Variables:
        target -> This one will fetch the user with the ID that will be given.

       *****************************************************************************************************************************************
       '''

    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)
            await ctx.channel.send("'" + args + "'" + " Foi enviada para: " + target.name)
        except:
            await ctx.channel.send("Não foi possível mandar a mensager")


## --------------------------------------- ##
@bot.command(name='alldm')
@commands.has_any_role('admin')
async def alldm(ctx, *, args=None):
    '''
      *****************************************************************************************************************************************

       ### Description: 
       When the command "!alldm(+ message you want to be sent)" is inserted, it sends a message to the private channel
       of all members in the server.

       ### Parameters:
       ctx -> Variable that receives the command; 
       args -> The message to be sent.

       ### Variables:
       member & members -> These will run through all of the members in the guild.

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
                    print("Não foi possível enviar '" +
                          args + "' para" + member.name)
    else:
        await ctx.channel.send("faltaram argumentos")

## --------------------------------------- ##


@bot.command(name='gtmin')
@commands.has_any_role('admin')
async def get_admins(ctx):
    '''
    *****************************************************************************************************************************************

     ### Description: 
     When the command "!gtmin" is inserted in the channel, it returns all the members with the "admin" role.

     ### Parameters:
     ctx -> Variable that receives the command. 

     ### Variables:
     role_name -> It is the name of a specific role of the guild;
     role -> This one will search/find that role with the given name;
     user -> This will run through the members;
     embed -> Message to be sent, but with the embed class. 

    *****************************************************************************************************************************************

    '''

    role_name = 'admin'
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
    embed = discord.Embed(title=f"Admins ", description='', color=0xDC143C)

    for user in ctx.guild.members:
        if role in user.roles:
            embed.add_field(
                name=user.name, value=f' possui o cargo: {role}', inline=False)

    await ctx.send(embed=embed)


## --------------------------------------- ##
@bot.command(name='gtaluno')
@commands.has_any_role('admin')
async def get_alunos(ctx):
    '''
    *****************************************************************************************************************************************

     ### Description: 
     When the command "!gtaluno" is inserted in the channel, it returns all the members with the "aluno" role.

     ### Parameters:
     ctx -> Variable that receives the command. 

     ### Variables:
     role_name -> It is the name of a specific role of the guild;
     role -> This one will search/find that role with the given name;
     user -> This will run through the members.

    *****************************************************************************************************************************************

    '''
    role_name = 'aluno'
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
    embed = discord.Embed(title=f"Alunos ", description='', color=0xDC143C)

    for user in ctx.guild.members:
        if role in user.roles:
            embed.add_field(
                name=user.name, value=f'possui o cargo: {role}', inline=False)

    await ctx.send(embed=embed)


## --------------------------------------- ##
@bot.command(name='msaluno')
@commands.has_any_role('admin')
async def msalunos(ctx, message):
    '''
     *****************************************************************************************************************************************

      ### Description: 
      It sends a message which will be inserted in the command, to all members with the "aluno" as a role. 

      ### Parameters:
      ctx -> variable that receives the command;
      message -> message to be sent.

      ### Variables:
      role_name -> it is the name of a specific role of the guild
      role -> this one will search/find that role with the given name
      user -> this will run through the members

     *****************************************************************************************************************************************
     '''

    role_name = 'aluno'
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
    members = ctx.guild.members

    for member in members:
        if role in member.roles:
            await member.send(message)


## --------------------------------------- ##
@bot.command(name='msadmin')
@commands.has_any_role('admin')
async def msalunos(ctx, message):
    '''
       *****************************************************************************************************************************************

        ### Description: 
        It sends a message to all members with the "admin" role. 

        ### Parameters:
        ctx -> variable that receives the command; 
        message -> the message which will be sent.

        ### Variables:
        role_name -> it is the name of a specific role of the guild;
        role -> this one will search/find that role with the given name;
        member -> this will run through the members. 

       *****************************************************************************************************************************************
   '''
    role_name = 'admin'
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
    members = ctx.guild.members

    for member in members:
        if role in member.roles:
            await member.send(message)


@bot.command(name='presenças')
async def presencas(ctx):
    '''
*****************************************************************************************************************************************

 ### Description: 
    This method writes, in a comma-separated values (CSV) file, the members who are not offiline in the guild,
    a Timestamp for the current hour, and the channel where the command was inserted.   

### Parameters:
    ctx -> variable that receives the command. 

### Variables:
    channel -> stores the channel where the message was sent;
    guild -> stores the current guild;
    now -> is the current time;
    now_time -> it is the current date, but formated with the date+hour to store in the CSV file;
    now_date -> it is only the current date, in the format "day/month/year";
    writer -> variable to write in the CSV file.

*****************************************************************************************************************************************
'''

    channel = ctx.message.channel
    guild = ctx.message.guild
    now = datetime.now(pytz.timezone('Europe/Lisbon'))
    now_time = now.strftime("%d/%m/%Y - %H:%M")
    now_date = now.strftime("%d/%m/%Y")

    with open('pres.csv', 'w', newline='') as file:
        file.write('Nome, Data e Hora, canal \n')
        writer = csv.writer(file, delimiter=',')
        for membros in guild.members:
            writer = csv.writer(file, delimiter='"')

            if membros.status != discord.Status.offline:
                writer.writerow(
                    [membros.name + ', ' + now_time + ', ' + str(channel.name)])

    await channel.send(f'Presenças da data: {now_date} ')
    await channel.send(file=discord.File('pres.csv'))


def filterOnlyBots(member):
    '''
     ### Description: 
     It is a filter that returns all the members which are bots

     ### Parameters: 
     member -> The members in the guild

    '''
    return member.bot


def filterOnlyOnlineMembers(member):
    '''
     ### Description: 
     It is a filter that returns the online members

     ### Parameters: 
     member -> The members in the guild

    '''
    return member.status != discord.Status.offline


@bot.command(name='status')
@commands.has_any_role('admin')
async def on_message(ctx):
    '''
*****************************************************************************************************************************************

### Description: 
    This method shows all the members, that are currently "not offiline" in the guild, 
    along with the total amount of members, and the amount of bots of the server. It calls the methods with return:
    "filterOnlyBots", "FilterOnlineMembers", which are used to filter only a certain data of the attribute

### Parameters:
    ctx -> variable that receives the command. 

### Variables:
    channel -> stores the channel where the message was sent;
    now -> is the current time;
    bots_In_Server -> is a list that stores data of the guild, but filtered to only return the name of bots;
    bots_Count -> it is the length of the botsInServer list. It is the amount of items in the list botsInServer; 
    namelist -> array that will store only the name of the members; 
    namesonlinelist -> array that will store only the name of the members that are not offiline; 
    timenow -> it is only the current date and time, in the format "day/month/year" + "Hour:Minute";
    onlineMembersInServer -> list of members that are not offiline;
    usersInServerCount -> Counts the amount of the "human" members in the server; 
    msg -> Is the class embed message to be sent.

*****************************************************************************************************************************************
'''
    now = datetime.now(pytz.timezone('Europe/Lisbon'))
    membersInServer = ctx.guild.members
    channel = ctx.message.channel
    bots_In_Server = list(filter(filterOnlyBots, membersInServer))
    bots_Count = len(bots_In_Server)
    namelist = []
    namesonlinelist = []
    timenow = now.strftime("%d/%m/%Y - %H:%M")
    onlineMembersInServer = list(
        filter(filterOnlyOnlineMembers, membersInServer))
    usersInServerCount = ctx.message.guild.member_count - bots_Count

    for items in onlineMembersInServer:
        namesonlinelist.append(items.name)
        online = "; \n".join(namesonlinelist) + '.'

    for item in membersInServer:
        namelist.append(item.name)
        names = "; \n".join(namelist) + '.'

    msg = discord.Embed(
        title=f"Presentes a {timenow}", description='', color=0xDC143C)

    msg.add_field(name="Quantidade de membros:",
                  value=usersInServerCount, inline=False)
    msg.add_field(name="Quantidade de bots:", value=bots_Count, inline=False)

    msg.add_field(name="Membros: \n", value=names, inline=True)
    msg.add_field(name="Membros Online: \n ", value=online, inline=True)
    await channel.send(embed=msg)


bot.run(TOKEN)
