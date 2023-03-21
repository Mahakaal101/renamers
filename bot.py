import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5945280153:AAEZFpMp-Plgwgoce0uVkT7RKk6rLTngCSA")

API_ID = int(os.environ.get("API_ID", "15823382"))

API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")

STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME", "renamer")

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")

BOT_USERNAME = os.environ.get("BOT_USERNAME", "tlgrenamerbot")

CHANNEL = os.environ.get("CHANNEL", "Film_Update_Official")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
