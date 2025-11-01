import os
import telebot

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 Welcome!\n\nSend /get <file_id> to receive your file.\n\nExample:\n/get BAACAgQAAxkBAA..."
    )

@bot.message_handler(commands=['get'])
def get_file(message):
    parts = message.text.split(" ")
    if len(parts) == 2:
        file_id = parts[1]
        try:
            bot.send_video(message.chat.id, file_id)
        except:
            try:
                bot.send_document(message.chat.id, file_id)
            except:
                bot.send_message(message.chat.id, "⚠️ Invalid File ID or File Type not supported.")
    else:
        bot.send_message(message.chat.id, "❗ Usage:\n/get <file_id>")

bot.infinity_polling()
