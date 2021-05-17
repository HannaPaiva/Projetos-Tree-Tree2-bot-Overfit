import os #
import os #
import discord
import time
from discord import message
from dotenv import load_dotenv 
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


now = datetime.now()

load_dotenv()
TOKEN = 'ODM5MTc2NzIxNzg4ODI5NzE4.YJF2OQ.pxogH1ju_2XKYjC_mbRj12RZQIw' 

client = discord.Client()
channel = client.get_channel(841977130208460821)


mensagem1 = f':books:  Bem-vindos à Prova de Simulação de hoje :books: \n Juntem-se ao canal de voz "Sala do 20" para começarmos :point_up: \n @aluno. \n Aceda em https://drive.google.com/file/d/1qAk76anqjpP-JVfI741ig3OgLeuzv-Q3/view?usp=sharing'

mensagem2 = 'Início da prova: 9h30 \n 1º período até às 11h15 \n 2º período até às 12h00 \n Final da prova: 12h30'

mensagem3 = ':alarm_clock:  Está concluído o primeiro período da prova. :alarm_clock: \n Se ainda não terminaste, podes continuar - o segundo período termina às 11h55. \n Se já terminaste, preenche o formulário de checkout: https://forms.gle/T9UCET2Bgyr3hMYi6. Assim que preencheres o formulário podes ir aproveitar o sábado :wink: \n No final do dia publicaremos no fórum um post com os links para os critérios de correção e para o formulário de avaliação. Lembra-te de submeter o formulário de avaliação até quarta-feira ao final do dia. \n Bom trabalho e bom fim-de-semana!'

mensagem4 = ' Está concluído o segundo período da prova. :alarm_clock: \n Se ainda não terminaste, podes continuar até às 12h25. Se já terminaste, preenche o formulário de check-out e bom fim-de-semana!'

mensagem5 =  'Overfitters, \n Deixamos aqui os critérios de classificação 4 da prova de simulação 1 de hoje para que possam completar a vossa correção. Submetam-na até quarta-feira ao final do dia, através deste formulário 4. \n Lembramos que a correção da vossa prova, algumas horas depois de a terem feito, é uma parte importante do processo de aprendizagem e da preparação para ficarem a conhecer o exame de trás para a frente. \n Podem também usar este tópico para discutir a prova - em particular, exercício especialmente complicados ou sobre os quais tenham ficado com algumas dúvidas. \n O 20 no exame está cada vez mais próximo! :man_student:'



@client.event
async def on_ready():
    print('Seu bot está conectado!')

@client.event
async def on_message(message):
    now = datetime.now() #atualizar tempo com o evento
    tempo = now.strftime("%H:%M") 
    id = client.get_guild(838746575396274219)
    channels = ["sala20"]
    
    if str(message.channel) in channels:

       if tempo != "21:23":
         if message.content == "!prova":
          # await message.channel.send(f"Agora são {tempo}")
          await message.channel.send(mensagem1)
          await asyncio.sleep(5)
          await message.channel.send(mensagem2)
          await asyncio.sleep(25)
          await message.channel.send(mensagem3)
          await asyncio.sleep(25)
          await message.channel.send(mensagem4)
          await asyncio.sleep(25)
          await message.channel.send(mensagem5)
client.run(TOKEN)
