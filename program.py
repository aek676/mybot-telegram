import os
from dotenv import load_dotenv
import telebot

load_dotenv()

# Get BotToken and CanalID
BOT_TOKEN = os.getenv('BOT_TOKEN')
CANAL_ID = os.getenv('CANAL_ID')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.send_message(chat_id='-1002256283371', text="Hola, este es un mensaje automatico del bot")


bot.infinity_polling()