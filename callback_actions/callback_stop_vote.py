from main import bot
import constants


def stop(c):
    bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
    bot.send_message(c.message.chat.id, constants.INFO_STOPPED)
