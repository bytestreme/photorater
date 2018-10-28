from main import bot


def upload(c):
    bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
