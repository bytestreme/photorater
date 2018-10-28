from telebot import types

import constants


# Help menu's close button
def reg_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    btns = [types.InlineKeyboardButton(text=constants.UPLOAD_OK, callback_data='upload')]
    keyboard.add(*btns)
    return keyboard
