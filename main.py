import os
import telebot
from telebot import types

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "INFILTRADOR ATIVADO.\nUse /gerar para receber seu vídeo.")

@bot.message_handler(commands=['gerar'])
def gerar_video(message):
    bot.send_chat_action(message.chat.id, 'upload_video')
    bot.send_message(message.chat.id, "Gerando vídeo viral...")

    bot.send_video(message.chat.id, open("video_infiltrador.mp4", 'rb'), caption="Você ainda acha que tem tempo?\n\nINFLITRADOS — A verdade não será gentil.")

bot.polling()
