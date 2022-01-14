from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update  # объект обновлений


# команда start
def start(update=Update, context=CallbackContext):
    update.message.reply_text("Hi User")


def echo(update=Update, context=CallbackContext):
    update.message.reply_text(update.message.text)


# запуск бота
def main():
    updater = Updater("606262492:AAEuiIHxmj1rxBsIHCU6N3JBEVbLHyITZ7I")  # токен бота
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()  # запускает процесс слушания сервера и обновления данных
    updater.idle()  # завершает процесс слушания сервера и обновления данных после остановки программы


main()
