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
    count = 0
    interval = datetime(year=now.year, month=now.month,
                        day=now.day, hour=2, minute=0, second=0)
    seconds_interval = ((interval.hour * 3600) +
                        (interval.minute * 60) + interval.second)
    print(f"Espaço de tempo para a limpeza = {interval.strftime('%H:%M:%S')}")

    while True:

        await asyncio.sleep(seconds_interval)
        for channel in guild.channels:
            async for _ in channel.history(limit=None):
                count = count + 1

                await channel.purge(limit=count)

                await channel.send(args)
                if channel.name == 'auditório':

                    await channel.send(argaud)

        break
