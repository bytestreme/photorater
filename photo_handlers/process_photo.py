from persistence.db_actions import db_ph_get, db_ph_set
from main import bot
import constants


def process_photo(message):
    status_db1 = db_ph_get(message.from_user.id, 1)
    status_db2 = db_ph_get(message.from_user.id, 2)
    status_db3 = db_ph_get(message.from_user.id, 3)

    if status_db1 == constants.DB_EMPTY_STR:
        bot.send_chat_action(message.from_user.id, constants.BOT_ACTION_TYPING)
        file_id = message.photo[len(message.photo) - 1].file_id
        db_ph_set(message.from_user.id, 1, file_id)
        bot.send_message(message.from_user.id, constants.PHOTO_FIRST_SUCCESS)
    else:
        if status_db2 == constants.DB_EMPTY_STR:
            bot.send_chat_action(message.from_user.id, constants.BOT_ACTION_TYPING)
            file_id = message.photo[len(message.photo) - 1].file_id
            db_ph_set(message.from_user.id, 2, file_id)
            bot.send_message(message.from_user.id, constants.PHOTO_SECOND_SUCCESS)
        else:
            if status_db3 == constants.DB_EMPTY_STR:
                bot.send_chat_action(message.from_user.id, constants.BOT_ACTION_TYPING)
                file_id = message.photo[len(message.photo) - 1].file_id
                db_ph_set(message.from_user.id, 3, file_id)
                bot.send_message(message.from_user.id, constants.PHOTO_THIRD_SUCCESS)
            else:
                bot.send_chat_action(message.from_user.id, constants.BOT_ACTION_TYPING)
                bot.send_message(message.from_user.id, constants.PHOTO_UPLOAD_LIMIT_FAIL)
