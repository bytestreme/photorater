from telebot import types
import constants


# Keyboard for Rate Navigation
def pages_keyboard(currID):
    keyboard = types.InlineKeyboardMarkup()
    btns = [types.InlineKeyboardButton(text=constants.VOTE_DOWN, callback_data='minus' + str(currID)),
            types.InlineKeyboardButton(text=constants.VOTE_STOP, callback_data='stop'),
            types.InlineKeyboardButton(text=constants.VOTE_UP, callback_data='plus' + str(currID))]
    keyboard.add(*btns)
    return keyboard
