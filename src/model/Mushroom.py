from telebot import types


class Mushroom:
    title = "Этот раздел пуст"

    def getKeybords():
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Microdosing💊", callback_data='Using')
        btn2 = types.InlineKeyboardButton("Shrooming🤪👽👻", callback_data='Effects')
        return markup.add(btn1, btn2)

    @staticmethod
    def sendMsg(bot, msg):
        bot.clear_step_handler_by_chat_id(chat_id=msg.chat.id)  # удаляем сообщение
        bot.delete_message(msg.chat.id, msg.id)
        bot.send_photo(msg.chat.id, Mushroom.getFile, caption=Mushroom.title, reply_markup=Mushroom.getKeybords())

    @staticmethod
    def getFile():
        return open('static/2023-06-02 17.53.16.jpg', 'rb')
