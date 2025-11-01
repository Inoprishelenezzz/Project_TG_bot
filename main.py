# Импорт библиотек
import telebot
from telebot import types


# Токен
token = '8335220900:AAE3aAK-1WD6P4mE4_EvL3t22NlTgrulV5U'
# Создание бота
bot = telebot.TeleBot(token)
# Задача основных переменных
data_base = {}


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Функциональный блок
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Привет, я бот, для регистрации напиши /reg')

@bot.message_handler(commands=["help"])
def help_message(message, res=False):
    bot.send_message(message.chat.id, 'Тебе нужна помощь')

@bot.message_handler(commands=["reg"])
def registration(message,res=False):
    bot.send_message(message.chat.id, "Привет! Давай знакомиться, как тебя зовут?")
    bot.register_next_step_handler(message, get_name)

@bot.message_handler(content_types=["text"])
def handle_text(message, res=False):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)   


def get_name(message):
    global data_base
    if message not in data_base:

bot.polling(none_stop=True, interval=0)