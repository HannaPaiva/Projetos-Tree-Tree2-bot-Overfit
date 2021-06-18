# Python Discord Bot 

 Trixsbot is a free, open-source, extensible bot for Discord servers built with Python, and it can be run in a cloud hosting facility like AWS or in your own computer. Using Trixsbot, you have total control of the code and functions of the bot, and you may use it as a foundation for your own project.  
The entire code is documented with docstrings, and it is explaining in detail what each thing does in the functions. Good luck!! Trixsbot is here to help you get started with it. :D
## Author

* **[Hanna Paiva](https://github.com/Hantriex)**

## Contributors

* **[Pedro Marcelino](https://github.com/pmarcelino)**
* **[João Coelho](https://github.com/joaopcoelho)**

## Bot commands and functions

 These are basically what Trixsbot can do. 
And keep in mind: all the names inside brackets are also part of the command. It is where you write an input. 

### Commands

 **!t [seconds]** - It sends a message and starts to count a timer with the given time in seconds;

 **!timer** - It starts to count a timer with a default time of 1 hour. You can change it in the code;

 **!cls** - Clear the channel where the message was sent; 

 **!greet** - It sends a greeting to the member who sent the message;

 **!dm [user_ID] [message]**  - It sends the message you write for a member with a certain ID;

 **!alldm "[message]"** - It sends the message you write to all the members in the server;

 **!contar_mensagens** - It counts how much messages are in a text channel;

 **!gtmin** - Returns all members with the "admin" role;

 **!gtaluno** - Returns all members with the "aluno" role;

 **!msadmin [message]** - It sends a message to all members with the "admin" role (you can change the name of the role in the code); 

 **!msaluno [message]** - It sends a message to all members with the "aluno" role;

 **!presenças** - It sends a .CSV file with the members who are not offiline, with the Timestamp and the channel where the command was given; 

 **!status** - It sends a message with the total of members in the server, total of bots in the server and the name of those who are online; 

 **!create [Name of the channel] [Name of the category]** - It creates a channel with the given name inside of the given category. Remember to write it with quotation marks;

 **!defcreate [Name of the channel]** - It creates a text channel in the default location of the method;

 **!delete [Name of the channel]** - It deletes the text channel with the given name;

 **!faq"** - It returns a link to a site with The Frequently Asked Questions about the server.

 ### functions
 
 The functions are methods that are always running as background processes while the bot is active. They are useful if you want your bot to do something in a given time, maybe daily or from time to time. You have to call them in the **On_Ready()** function. 
All of these methods can be found separeted in the folder "Single Commands and methods", and you can change the value of the variables as you wish. 

**DailyCleanup()** - This method erases all the messages every day in a given time, in all text channels in the guild, and it 
     is called when the bot starts. It is also always running as a background process.
     
**AsyncioCleanup()** - This method erases all the messages in all text channels in the guild and it is called when the bot starts. The cleaning is done from time to time (x to x time // like from 2 to 2 hours)

**Reminder()** - This method has the purpose to send messages to the private chat of the guild members with a specific role at a certain time. In this case, when the time is the same as the one assigned to the 'reminder' variable, it sends a message to all students with the given role name, attached to a timer that shows how much time is left for the server activities to start. 

## How to download and use it

This repository contains a code which you can download and build your own bot with it, by cloning/Downloading the repository, and switching the content of some variables.
You also can check [this tutorial](https://realpython.com/how-to-make-a-discord-bot-python/) about creating your own bot in python. Follow the steps and paste the code. 

## Variables that ***must*** have its value changed

In the code, you ***have*** to locate and change these:

| Variable              | What it is                                                            |
| ----------------------| ----------------------------------------------------------------------|
| TOKEN                 | It is the token of your bot, that it also can be stored in another file.|
| GUILD                 | Here, you put the name of your server/guild. |
| PREFIX                | The letter/sign your commands will have before it.|




## To install with pip install


```
pip install discord
```
```
pip install asyncio
```
```
pip install pytz 
```
The last one is optional if you are not hosting your bot anywhere.


## Issues or Questions

Here on [Trixsbot](https://github.com/Hantriex/Projetos-Tree-Tree2--Hanna-Paiva/issues/1)

## Built With

* [Python 3.8](https://www.python.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
