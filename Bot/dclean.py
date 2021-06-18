import discord
from discord.ext import commands
from datetime import datetime
import pytz
import discord.utils


GUILD = 'Teste'
TOKEN = 
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
guild = discord.utils.get(bot.guilds, name=GUILD)
strtimecleanup = '08:00'




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

 async def on_ready():
    ''' 
    *****************************************************************************************************************************************

    ### Description: 
     The on_ready method is the method that runs when the bot is ready to be used/connected.
     it is calling the AsyncioCleanup() method, the Daily Cleanup method, and the Reminder() method;

    *****************************************************************************************************************************************
    '''
    print(f'{bot.user.name} irá limpar todos os canais de tempo em tempo')
    await  Daily_Cleanup()


bot.run(TOKEN)
    
