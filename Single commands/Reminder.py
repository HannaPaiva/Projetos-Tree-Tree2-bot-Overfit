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
            
