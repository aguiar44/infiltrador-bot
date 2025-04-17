
import os
import telebot

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "INFILTRADOR ATIVADO.\nUse /gerar para receber seu vídeo.")

@bot.message_handler(commands=['gerar'])
def gerar_video(message):
    bot.send_chat_action(message.chat.id, 'upload_video')
    bot.send_message(message.chat.id, "Gerando vídeo viral...")

    try:
        with open("video_infiltrador.mp4", "rb") as video:
            bot.send_video(message.chat.id, video, caption="Você ainda acha que tem tempo?\n\nINFLITRADOS — A verdade não será gentil.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ocorreu um erro ao enviar o vídeo: {e}")

if __name__ == "__main__":
    print("INFILTRADOR INICIADO. Aguardando comandos...")
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")
