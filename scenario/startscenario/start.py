from telebot import types

import constants
from main import bot
from persistence.db_actions import store


def start(message):
    checker = store(message.from_user.id, message.from_user.username, message.from_user.first_name,
                    message.from_user.last_name)
    user_markup = types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Неlр', 'Rаtе', 'Рrоfilе')
    if checker:
        bot.send_message(message.from_user.id, 'ID:' + str(message.from_user.id) + ' profile found.',
                         reply_markup=user_markup)
    else:
        bot.send_message(message.from_user.id, 'ID:' + str(message.from_user.id) + ' profile created.',
                         reply_markup=user_markup)
        bot.send_message(message.from_user.id, constants.INFO_DEV)
