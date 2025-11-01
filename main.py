# Импорт библиотек
import telebot
from telebot import types


# Токен
token = "токен"
# Создание бота
bot = telebot.TeleBot(token)
# Задача основных переменных
data_base = {}

# Класс человека
class Person:
    def __init__(self, name):
        self.name = name

# Функциональный блок
@bot.message_handler(commands=["start"])
def start(message, res=False): # Приветственное сообщение
    keyboard_start = types.InlineKeyboardMarkup()
    key_reg = types.InlineKeyboardButton(text="Зарегестрироваться", callback_data="reg")
    keyboard_start.add(key_reg)
    key_help = types.InlineKeyboardButton(text="Помощь", callback_data="help")
    keyboard_start.add(key_help)
    key_menu = types.InlineKeyboardButton(text="Главное меню", callback_data="menu")
    keyboard_start.add(key_menu)
    bot.send_message(message.chat.id, 'Привет, я бот, для регистрации напиши /reg, если что-то не понятно напиши /help и попробуем разобраться!', reply_markup=keyboard_start)
    

@bot.message_handler(commands=["help"])
def help(message, res=False): # Помощь
    bot.send_message(message.chat.id, "Вам нужна помощь")
    print(message.chat.id)
    print(data_base)


@bot.message_handler(commands=["reg"])
def registration(message,res=False): # Регистрация
    global data_base
    if message.chat.id not in data_base:
        bot.send_message(message.chat.id, "Как я могу к Вам обращаться?")
        bot.register_next_step_handler(message, get_name)
    else:
        print("h")
        keyboard_new_register = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Да", callback_data="reg_yes")
        keyboard_new_register.add(key_yes)
        key_no = types.InlineKeyboardButton(text="Нет", callback_data="reg_no")
        keyboard_new_register.add(key_no)
        bot.send_message(message.chat.id, "Мы с Вами уже знакомы, хотите поменять имя в системе?", reply_markup=keyboard_new_register)


    


@bot.message_handler(content_types=["text"])
def handle_text(message, res=False): # Обработка текста
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)   


@bot.message_handler(commands=["/menu"])
def main_menu(message, res=False): # Главное меню
    bot.send_message(message.chat.id, "Это главное меню")


def get_name(message):
    global data_base
    data_base[message.chat.id] = Person(message)
    print(data_base)
    

def rename(message): 
    data_base[message.chat.id] = Person(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global data_base, registration, main_menu, help
    if call.data == "reg": 
        registration(call.message)
    elif call.data == "help":
        help(call.message)
    elif call.data == "menu" or call.data == "reg_no":
        main_menu(call.message)
    elif call.data == "reg_yes":
        bot.send_message(call.message.chat.id, "Как я могу к Вам обращаться?")
        bot.register_next_step_handler(call.message, rename)
        
        

bot.polling(none_stop=True, interval=0)