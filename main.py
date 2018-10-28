import telebot
from flask import Flask
from flask import request
from telebot import types

import config
import constants
from callback_actions.callback_dislike import callback_dislike
from callback_actions.callback_like import callback_like
from callback_actions.callback_lnk import lnk
from callback_actions.callback_stop_vote import stop
from callback_actions.callback_upload import upload
from callback_actions.callback_warn import callback_warn
from callback_actions.delete_actions import del_actions
from callback_actions.profile_actions import profile_actions
from photo_handlers.process_photo import process_photo
from scenario.menuscenario import menu
from scenario.startscenario import start

bot = telebot.TeleBot(config.token, threaded=False)

server = Flask(__name__)


@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return constants.html_template, 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.webhook_url + config.token)
    return constants.html_template, 200


# Start command handler: Send Main Keyboard
@bot.message_handler(commands=['start'])
def handle_start(message):
    start(message)


# Send message from Reply Markup
@bot.message_handler(content_types=['text'])
def menu_handler(m):
    menu(m)


# Callback data handler
@bot.callback_query_handler(func=lambda c: c.data)
def pages(c):
    # Add like to Photo's User and add VotesNumber to Voting User
    if c.data.startswith('plus'):
        callback_like(c)

    # Add Dislike to Photo's User and add VotesNumber to Voting User
    elif c.data.startswith('minus'):
        callback_dislike(c)

    # Delete Help message
    elif c.data == 'upload':
        upload(c)

    # Srop Voting
    elif c.data == 'stop':
        stop(c)

    # Link to Rate from inline button if VotesNumber are not enough
    elif c.data == 'warn':
        callback_warn(c)

    # Delete message with vote number and opens Profile
    elif c.data == 'lnk':
        lnk(c)

    elif c.data.startswith('p_'):
        profile_actions(c)

    elif c.data.startswith('del'):
        del_actions(c)


# Handles Photos or Images if they were sent by user. Does not add if three are already uploaded
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    process_photo(message)


if __name__ == "__main__":
    server.run()
