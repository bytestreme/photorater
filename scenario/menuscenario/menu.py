import constants
from keyboard.profile.profile_kb_builder import warn_key, lnk_key
from keyboard.rate.rating_kb_builder import pages_keyboard
from keyboard.upload.upload_kb_builder import reg_keyboard
from main import bot
from persistence.db_actions import db_ph_get, db_rand_get
from persistence.db_actions import intersection
from persistence.vote.db_vote import db_votelist_update, db_votedlist_get, db_votelist_get, db_vote_get


def main_menu(m):
    if m.text == constants.MENU_RATE:
        db_votelist_update(m.from_user.id)
        bot.send_chat_action(m.from_user.id, constants.BOT_ACTION_PH_UPLOAD)
        someID = db_votelist_get(m.from_user.id)
        notID = db_votedlist_get(m.from_user.id)
        ntrsc = intersection(someID, notID)
        if len(ntrsc) == someID:
            bot.send_message(m.from_user.id, constants.NO_NEW_PHOTOS)
            return
        else:
            for t in ntrsc:
                someID.remove(t)
            try:
                currID = int(someID[0])
                usrrand = db_rand_get(m.from_user.id)
                idtovote = db_ph_get(currID, usrrand)
                bot.send_photo(m.from_user.id, idtovote, reply_markup=pages_keyboard(currID))
            except IndexError:
                bot.send_message(m.from_user.id, constants.NO_NEW_PHOTOS)
    if m.text == constants.MENU_HELP:
        bot.send_chat_action(m.from_user.id, constants.BOT_ACTION_TYPING)
        bot.send_message(m.from_user.id, constants.HELP_TEXT, reply_markup=reg_keyboard())
    if m.text == constants.MENU_PROFILE:
        if db_vote_get(m.from_user.id) is not None:
            if db_vote_get(m.from_user.id) < 5:
                bot.send_message(m.from_user.id, constants.POINTS_NOT_ENOUGH,
                                 reply_markup=warn_key(m.from_user.id))
            else:
                bot.send_message(m.from_user.id, constants.POINTS_ENOUGH,
                                 reply_markup=lnk_key(m.from_user.id))
