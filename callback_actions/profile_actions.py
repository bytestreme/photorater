import constants
from keyboard.profile.profile_kb_builder import my_page_keyboard, my_keyboard, del_keyboard, del_page_keyboard, \
    prof_keyboard
from main import bot
from persistence.db_actions import db_ph_get, db_value_get
from persistence.vote.db_vote import db_vote_get


def profile_actions(c):
    # Close Profile by deleting message with it
    if c.data == 'p_close':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, constants.INFO_CLOSED)

    # DELETE OPTION
    elif c.data == 'p_del':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, constants.DEL_SELECT, reply_markup=del_keyboard())

    elif c.data == 'p_del_1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        sphoto = db_ph_get(c.from_user.id, 1)
        has = 1
        if sphoto == constants.DB_EMPTY_STR:
            has = 0
            sphoto = constants.NO_PHOTO_1_ID  # NONE 1 PHOTO
        bot.send_photo(c.from_user.id, sphoto, reply_markup=del_page_keyboard(1, has))

    elif c.data == 'p_del_2':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        sphoto = db_ph_get(c.from_user.id, 2)
        has = 1
        if sphoto == constants.DB_EMPTY_STR:
            has = 0
            sphoto = constants.NO_PHOTO_2_ID  # NONE 2 PHOTO
        bot.send_photo(c.from_user.id, sphoto, reply_markup=del_page_keyboard(2, has))

    elif c.data == 'p_del_3':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        sphoto = db_ph_get(c.from_user.id, 3)
        has = 1
        if sphoto == constants.DB_EMPTY_STR:
            has = 0
            sphoto = constants.NO_PHOTO_3_ID  # NONE 3 PHOTO
        bot.send_photo(c.from_user.id, sphoto, reply_markup=del_page_keyboard(3, has))

    elif c.data == 'p_my':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, constants.DEL_SELECT, reply_markup=my_keyboard())

    elif c.data == 'p_my_1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        sphoto = db_ph_get(c.from_user.id, 1)
        has = 1
        if sphoto == constants.DB_EMPTY_STR:
            has = 0
            sphoto = constants.NO_PHOTO_1_ID  # NONE 1 PHOTO
        bot.send_photo(c.from_user.id, sphoto, reply_markup=my_page_keyboard())

    elif c.data == 'p_my_2':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        sphoto = db_ph_get(c.from_user.id, 2)
        has = 1
        if sphoto == constants.DB_EMPTY_STR:
            has = 0
            sphoto = constants.NO_PHOTO_2_ID  # NONE 2 PHOTO
        bot.send_photo(c.from_user.id, sphoto, reply_markup=my_page_keyboard())
    elif c.data == 'p_my_3':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        sphoto = db_ph_get(c.from_user.id, 3)
        has = 1
        if sphoto == constants.DB_EMPTY_STR:
            has = 0
            sphoto = constants.NO_PHOTO_3_ID  # NONE 3 PHOTO
        bot.send_photo(c.from_user.id, sphoto, reply_markup=my_page_keyboard())

    elif c.data == 'p_to_my':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "*ID:" + str(c.from_user.id) + " Profile*" + "\n" + "Vote points: " + str(
            db_vote_get(c.from_user.id)) + "\n" + constants.LIKE_DISLIKE + str(
            db_value_get(c.from_user.id, "like")) + "|" + str(db_value_get(c.from_user.id, "dislike")),
                         parse_mode="Markdown", reply_markup=prof_keyboard())
