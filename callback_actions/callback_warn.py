from main import bot
from persistence.vote.db_vote import db_votelist_get, db_votelist_update
from persistence.db_actions import db_rand_get, db_ph_get
from keyboard.rate.rating_kb_builder import pages_keyboard
import constants


def callback_warn(c):
    db_votelist_update(c.from_user.id)
    someID = db_votelist_get(c.from_user.id)  # list of ids to vote
    currID = int(someID[0])
    if currID is None:
        bot.send_message(c.from_user.id, constants.NO_NEW_PHOTOS)
        return
    bot.send_chat_action(c.from_user.id, 'upload_photo')
    usrrand = db_rand_get(c.from_user.id)
    idtovote = db_ph_get(currID, usrrand)
    bot.send_photo(c.from_user.id, idtovote, reply_markup=pages_keyboard(currID))
