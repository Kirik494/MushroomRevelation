# -*- coding: utf-8 -*-
import telebot
from telebot import types
import mysql.connector

from src.model.Amanita import Amanita
from src.model.Mushroom import Mushroom
from src.model.Rape import Rape

bot = telebot.TeleBot("6133847062:AAGbjK-paipNHgdU7q0aq-xYQs4AbL9kEL0")
db = mysql.connector.connect(host='127.0.0.1', user='root', password='root', port=3306, database='db')
cursor = db.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)  # удаляем сообщение
    bot.delete_message(message.chat.id, message.id)  # удаляем сообщение
    sql_select = "SELECT * FROM user WHERE tg_id = %s"  # Составляем запрос для бд
    td_id = (message.from_user.id,)
    cursor.execute(sql_select, td_id)  # Выполняем запрос
    result = cursor.fetchone()  # записываем результат

    if result is None:  # проверяем если не было такого юзера, то записываем его в бд
        sql_insert = "INSERT INTO user (tg_id, user_name) VALUES(%s, %s)"
        cursor.execute(sql_insert,
                       (message.from_user.id, message.from_user.username))
        db.commit()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🍄Fly agaric🍄")
    btn2 = types.KeyboardButton("🌈Magic mushrooms✨")
    btn3 = types.KeyboardButton("🪬Rape🗿")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,
                     "Братишка " + message.from_user.username + ", добро пожаловать👋", reply_markup=markup)


@bot.message_handler(content_types=['text', 'photo'])
def get_text_messages(message):
    match message.text:
        case "🍄Fly agaric🍄":
            Amanita.sendMsg(bot, message)
        case "🌈Magic mushrooms✨":
            Mushroom.sendMsg(bot, message)
        case "🪬Rape🗿":
            Rape.sendMsg(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    splitStr = call.data.split('_')
    obj = splitStr[0]
    mthd = splitStr[1]
    match obj:
        case 'amanita':
            if mthd == 'return':
                Amanita.sendMsg(bot, call.message)
            else:
                Amanita.sendResp(bot, call.message, mthd)


bot.polling(none_stop=True, interval=0)
