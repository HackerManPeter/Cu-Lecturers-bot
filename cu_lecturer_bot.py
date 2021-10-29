import logging
import os
TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', 5000))

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from cu_web_scrapper import call_lecturer

logging.basicConfig(
    format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger=logging.getLogger(__name__)


def start(update: Update, context:CallbackContext):
    update.message.reply_text('hi')

def help_command(update: Update, context:CallbackContext):
    update.message.reply_text('help')


def send_lecturer(update: Update, context:CallbackContext):
    text = update.message.text
    user_message = call_lecturer(text)
    for item in range(len(user_message)):
        update.message.reply_text(user_message[item])


def main():
    updater =  Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, send_lecturer))

    # updater.start_polling()
    updater.start_webhook(
        listen='0.0.0.0',
        port=int(PORT),
        url_path=TOKEN
    )
    updater.bot.setWebhook('https://cu-lecturers-bot.herokuapp.com/' + TOKEN)
    

    updater.idle()

if __name__ == '__main__':
    main()