from telebot import types


class Rape:
    title = "Этот раздел пуст"

    def getKeybords():
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Using🪬", callback_data='Using')
        btn2 = types.InlineKeyboardButton("Effects🗿", callback_data='Effects')
        btn3 = types.InlineKeyboardButton("Product", callback_data='Effects')
        return markup.add(btn1, btn2, btn3)

    @staticmethod
    def sendMsg(bot, msg):
        bot.clear_step_handler_by_chat_id(chat_id=msg.chat.id)  # удаляем сообщение
        bot.delete_message(msg.chat.id, msg.id)
        bot.send_message(msg.chat.id, Rape.title, reply_markup=Rape.getKeybords())

