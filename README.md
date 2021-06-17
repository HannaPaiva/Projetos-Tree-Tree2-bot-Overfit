# Python Discord Bot 

Trixsbot is a free, open-source, extensible bot for Discord servers, built with Python, and it can be run in a cloud hosting facility like AWS or in your own computer. Using Trixsbot, you have total control of the code and functions of the bot, and may use it as a foundation for your own project. 

## Author

* **[Hanna Paiva](https://github.com/Hantriex)**

## Contributors

* **[Pedro Marcelino](https://github.com/pmarcelino)**
* **[João Coelho](https://github.com/joaopcoelho)**

## Bot functions

**!t <segundos>** - Começa a contar um timer com o tempo estabelecido (em segundos);
**!timer** - O timer conta o tempo atribuído como *default*;
**!cls** - Limpa o canal de texto;
**!greet** - Envia uma mensagem privada de "Olá!! :D para o autor da mensagem";
**!dm <user_ID> <mensagem>**  - Envia uma mensagem privada para um membro específico do servidor;
**!alldm <mensagem>** - Envia mensagem para todos os membros do servidor;
**!contar_mensagens** - Conta quantas mensagens há num canal de texto;
**!gtmin** - Devolve todos os que têm o cargo de "admin";
**!gtaluno** - Devolve todos os que têm o cargo de "aluno";
**!msadmin** - Envia mensagem para todos os membros que são "admin";
**!msaluno** - Envia mensagem para todos os membros que são "admin";
**!presenças** - Envia um ficheiro .CSV com as presenças, o canal, e um Timestamp;
**!status** - Envia uma mensagem com o total de membros, total de bots, e os membros que estão online; 
**!create <nome do canal> <categoria>** - Cria um canal com o nome inserido, na categoria inserida (Se houver emojis ou espaços, escrever entre aspas);
**!defcreate <nome do canal>** - Cria um canal no topo de todos os canais;
**!delete <nome do canal>** - Apaga um canal de texto.
  
## How to download it

This repository contains a code which you can download and build your own bot with it, by cloning/Downloading the repository, and switching the content of some variables.


## Variables that must have its value changed

In the code, you have to locate and change these:

| Variable              | What it is                                                            |
| ----------------------| ----------------------------------------------------------------------|
| TOKEN                 | It is the token of your bot, that it also can be stored in another file. Never share this|
| GUILD                 | Here, you put the name of your server/guild |
| PREFIX                | The letter/sign your commands will have before it|




## How to start


```
pip install discord
```
```
pip install asyncio
```
```
pip install pytz
```


## Issues or Questions

---

## Built With

* [Python 3.8](https://www.python.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
