from main import bot
from persistence.vote.db_vote import db_vote_get, db_vote_set, db_vote_not_voted_get
from persistence.like.db_like import db_dislike_get, db_dislike_set
from persistence.db_actions import db_value_get, db_value_set, db_rand_get, db_ph_get
from keyboard.rate.rating_kb_builder import pages_keyboard
import constants


def callback_dislike(c):
    bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
    db_vote_set(c.from_user.id, db_vote_get(c.from_user.id) + 1)
    nowid = int(c.data[-9:])
    db_dislike_set(nowid, db_dislike_get(nowid) + 1)
    cvlst = db_value_get(c.from_user.id, "votedlist")
    if cvlst is not None:  # Get current votedlist
        db_value_set(c.from_user.id, "votedlist", cvlst + str(nowid) + '\n')
    else:
        db_value_set(c.from_user.id, "votedlist", str(nowid) + '\n')
    currID = db_vote_not_voted_get(c.from_user.id)
    if currID is None:
        bot.send_message(c.from_user.id, constants.NO_NEW_PHOTOS)
        return
    bot.send_chat_action(c.from_user.id, 'upload_photo')
    usrrand = db_rand_get(c.from_user.id)
    idtovote = db_ph_get(currID, usrrand)
    bot.send_photo(c.message.chat.id, idtovote, reply_markup=pages_keyboard(currID))
