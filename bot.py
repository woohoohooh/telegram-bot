from config import token
import telebot

bot = telebot.TeleBot(token)
name = ''

@bot.message_handler(commands=['start'])
def start_com(message):
    poem = 'Привет!\nЗаполните анкету на создание лэндинга дляоценки'
    bot.send_message(message.chat.id, poem)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f'yo {name}, sent /push')

@bot.message_handler(content_types=['text'])
def start_com(message):
    if message == 'ok':
        bot.send_message(message.chat.id, message)

bot.polling()