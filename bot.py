import telebot
from flask import Flask, request

BOT_TOKEN = "YOUR_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Bot is running ✅")

@app.route('/' + BOT_TOKEN, methods=['POST'])
def receive_update():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/')
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://YOUR_RENDER_SERVICE_URL/" + BOT_TOKEN)
    return "Webhook set ✅", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
