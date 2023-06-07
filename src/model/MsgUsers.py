users = {}


class MsgUsers:
    def add_msg_to_list(uid: int, msg_id: int):
        if uid in users:
            users[uid].append(msg_id)
        else:
            users[uid] = [msg_id, ]

    def remove_msg(chat_id, msg_id):
        for msg_id in users[chat_id]:
            bot.delete_message(
                chat_id=chat_id,
                message_id=msg_id,
            )
