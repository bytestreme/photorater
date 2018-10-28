from main import bot
from persistence.vote.db_vote import db_votelist_update, db_votedlist_get, db_votelist_get, db_vote_get
from persistence.db_actions import intersection
from persistence.db_actions import db_ph_get, db_rand_get
from keyboard.upload.upload_kb_builder import reg_keyboard
from keyboard.rate.rating_kb_builder import pages_keyboard
from keyboard.profile.profile_kb_builder import warn_key, lnk_key

def main_menu(m):
    if m.text == "Rаtе":
        db_votelist_update(m.from_user.id)
        bot.send_chat_action(m.from_user.id, 'upload_photo')
        someID = db_votelist_get(m.from_user.id)
        notID = db_votedlist_get(m.from_user.id)
        ntrsc = intersection(someID, notID)
        if len(ntrsc) == someID:
            bot.send_message(m.from_user.id, "You have voted on all available users")
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
                bot.send_message(m.from_user.id, "You have voted on all available users")
    if m.text == "Неlр":
        bot.send_chat_action(m.from_user.id, 'typing')
        bot.send_message(m.from_user.id,
                         "First, register by sending your photos (3 photos can be set by attachment or camera icons)\nSecond, like or dislike other photos (Rate) to earn vote points\nThird, in your Profile you can see your like and dislike number (From rating your photos by other people)\nFourth, to get access to Profile you must have at least 5 vote points.\nFifth, each time you enter your profile 5 points will be withdrawn.",
                         reply_markup=reg_keyboard())
    if m.text == "Рrоfilе":
        if db_vote_get(m.from_user.id) is not None:
            if db_vote_get(m.from_user.id) < 5:
                bot.send_message(m.from_user.id, "You haven't voted enough to view your Profile.",
                                 reply_markup=warn_key(m.from_user.id))
            else:
                bot.send_message(m.from_user.id, "You have voted enough to see your profile.",
                                 reply_markup=lnk_key(m.from_user.id))



