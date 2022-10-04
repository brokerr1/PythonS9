from logging import Filter
from tracemalloc import start
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5750066702:AAGYdNJBGumvmuYaW8_eWh8gy1yv3uYAZZ4')
updater = Updater(token='5750066702:AAGYdNJBGumvmuYaW8_eWh8gy1yv3uYAZZ4')
dispatcher = updater.dispatcher


def start(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, f'Привет это бот с домашним заданием для GeekBrains')

def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, del_some_words(text))

#удаление из текста всех слов, содержащих "абв". (текст вводит пользователь)
def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()