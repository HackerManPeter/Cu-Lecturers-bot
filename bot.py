import telebot

bot = telebot.TeleBot('1530520046:AAESyVrR1CeOKjH7Zx_RA-HPj6T2joh9AU4')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello there")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.id)

bot.infinity_polling()