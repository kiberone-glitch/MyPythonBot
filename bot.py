import telebot
import time
from telebot import types 




TOKEN = "FuckThis"


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup ()
    btn = types.InlineKeyboardButton ("О боте",callback_data="about")
    btn2 = types.InlineKeyboardButton ("Помощь",callback_data="help")
    btn3 = types.InlineKeyboardButton ("Поговорить с ботом", callback_data="talk")
    btn4 = types.InlineKeyboardButton ("Перезапуск", callback_data="start")
    markup.add (btn,btn2)
    markup.add (btn3)
    markup.add (btn4)
    bot.send_chat_action (message.chat.id, 'typing')
    time.sleep (2)
    bot.send_message(message.chat.id, "Привет, это бот Егора",reply_markup=markup)

@bot.callback_query_handler (func=lambda call2: True)
def callback2 (call2):
    if call2.data == "about":
        bot.send_chat_action (call2.message.chat.id, 'typing')
        time.sleep (2)
        bot.send_message (call2.message.chat.id, "Это бот Егора, написан на Python ")
    elif call2.data == "help":
        bot.send_chat_action (call2.message.chat.id, 'typing')
        time.sleep (2)
        bot.send_message (
             call2.message.chat.id,
             'Этот бот был сделан Егором 14.03.26. Бот был написан на python. Хостится на Railway. Также есть репозиторий на <a href="https://github.com/kiberone-glitch/MyPythonBot">Github</a>',
             parse_mode="HTML"
        )
        
    elif call2.data == "talk":
        bot.send_chat_action (call2.message.chat.id, 'typing')
        time.sleep (2)
        bot.send_message (call2.message.chat.id, "Привет ✌")
    elif call2.data == "start":
        start (call2.message)   

@bot.message_handler(content_types=['text'])
def chat(message):

    if message.text.lower() == "привет":
            bot.send_chat_action (message.chat.id, 'typing')
            time.sleep (2)
            bot.send_message(message.chat.id, "Привет, как дела?")

    elif message.text.lower () == "нормально":
            bot.send_chat_action (message.chat.id, 'typing')
            time.sleep (2)
            bot.send_message (message.chat.id, "Понятно")

    else:
        bot.send_chat_action (message.chat.id, 'typing')
        time.sleep (2)
        bot.send_message (message.chat.id, "Прости, я не понимаю тебя :( ")

                     


while True:
    try:
        print("Бот запущен...")
        bot.infinity_polling (skip_pending=True)

    except KeyboardInterrupt:
        print ("Бот остановлен...")
        break

    except Exception as e:
        print("Ошибка:", e)
        time.sleep(3)    
