from main import bot
from persistence.db_actions import db_value_set, db_value_get, db_ph_get, db_ph_set
from keyboard.profile.profile_kb_builder import prof_keyboard
from persistence.vote.db_vote import db_vote_get
import constants


def del_actions(c):
    if c.data == 'del_to_prof':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "*ID:" + str(c.from_user.id) + " Profile*" + "\n" + "Vote points: " + str(
            db_vote_get(c.from_user.id)) + "\n" + constants.LIKE_DISLIKE + str(
            db_value_get(c.from_user.id, "like")) + "|" + str(db_value_get(c.from_user.id, "dislike")),
                         parse_mode="Markdown", reply_markup=prof_keyboard())

    elif c.data == 'delete_photo1':
        db_ph_set(c.from_user.id, 1, "None")
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "*ID:" + str(c.from_user.id) + " Profile*" + "\n" + "Vote points: " + str(
            db_vote_get(c.from_user.id)) + "\n" + constants.LIKE_DISLIKE + str(
            db_value_get(c.from_user.id, "like")) + "|" + str(db_value_get(c.from_user.id, "dislike")),
                         parse_mode="Markdown", reply_markup=prof_keyboard())

    elif c.data == 'delete_photo2':
        db_ph_set(c.from_user.id, 2, "None")
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "*ID:" + str(c.from_user.id) + " Profile*" + "\n" + "Vote points: " + str(
            db_vote_get(c.from_user.id)) + "\n" + constants.LIKE_DISLIKE + str(
            db_value_get(c.from_user.id, "like")) + "|" + str(db_value_get(c.from_user.id, "dislike")),
                         parse_mode="Markdown", reply_markup=prof_keyboard())

    elif c.data == 'delete_photo3':
        db_ph_set(c.from_user.id, 3, "None")
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "*ID:" + str(c.from_user.id) + " Profile*" + "\n" + "Vote points: " + str(
            db_vote_get(c.from_user.id)) + "\n" + constants.LIKE_DISLIKE + str(
            db_value_get(c.from_user.id, "like")) + "|" + str(db_value_get(c.from_user.id, "dislike")),
                         parse_mode="Markdown", reply_markup=prof_keyboard())
