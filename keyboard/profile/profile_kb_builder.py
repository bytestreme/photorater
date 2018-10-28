from telebot import types
from persistence.vote.db_vote import db_vote_get


# Profile Keyboard:
def prof_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='My photos...', callback_data='p_my'))
    keyboard.row(types.InlineKeyboardButton(text='Delete photo...', callback_data='p_del'))
    keyboard.row(types.InlineKeyboardButton(text='Close', callback_data='p_close'))
    return keyboard


def del_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='Profile...', callback_data='del_to_prof'))
    keyboard.row(types.InlineKeyboardButton(text='Photo 1', callback_data='p_del_1'))
    keyboard.row(types.InlineKeyboardButton(text='Photo 2', callback_data='p_del_2'))
    keyboard.row(types.InlineKeyboardButton(text='Photo 3', callback_data='p_del_3'))
    return keyboard


def my_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='Profile...', callback_data='p_to_my'))
    keyboard.row(types.InlineKeyboardButton(text='Photo 1', callback_data='p_my_1'))
    keyboard.row(types.InlineKeyboardButton(text='Photo 2', callback_data='p_my_2'))
    keyboard.row(types.InlineKeyboardButton(text='Photo 3', callback_data='p_my_3'))
    return keyboard


def del_page_keyboard(number, has):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='Back...', callback_data='p_del'))
    if has != 0:
        keyboard.row(types.InlineKeyboardButton(text='Delete', callback_data='delete_photo' + str(number)))
    return keyboard


def my_page_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='Back...', callback_data='p_my'))
    return keyboard


# Link to Rate if VoteNumber is NOT enough
def warn_key(id):
    keyboard = types.InlineKeyboardMarkup()
    btns = [types.InlineKeyboardButton(
        text='You don\'t have enough vote points (' + str(db_vote_get(id)) + '). Tap to start voting',
        callback_data='warn')]
    keyboard.add(*btns)
    return keyboard


# Link to Profile if VoteNumber is sufficient
def lnk_key(id):
    keyboard = types.InlineKeyboardMarkup()
    btns = [types.InlineKeyboardButton(
        text='You have enough vote points (' + str(db_vote_get(id)) + '). ' + '\n' + 'Tap to enter Profile... (-5)',
        callback_data='lnk')]
    keyboard.add(*btns)
    return keyboard
