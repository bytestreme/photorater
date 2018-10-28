from telebot import types
from persistence.db_actions import store
from main import bot


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
        bot.send_message(message.from_user.id,
                         'This bot is in developing stage, so number of your vote points was set to 99 so that you can access your profile. You can still earn them by Rating others')
