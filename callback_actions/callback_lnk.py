import constants
from keyboard.profile.profile_kb_builder import prof_keyboard
from main import bot
from persistence.db_actions import db_value_get
from persistence.vote.db_vote import db_vote_get, db_vote_set


def lnk(c):
    bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
    db_vote_set(c.from_user.id, db_vote_get(c.from_user.id) - 5)
    bot.send_message(c.message.chat.id, "*ID:" + str(c.from_user.id) + " Profile*" + "\n" + "Vote points: " + str(
        db_vote_get(c.from_user.id)) + "\n" + constants.LIKE_DISLIKE + str(
        db_value_get(c.from_user.id, "like")) + "|" + str(db_value_get(c.from_user.id, "dislike")),
                     parse_mode="Markdown", reply_markup=prof_keyboard())
