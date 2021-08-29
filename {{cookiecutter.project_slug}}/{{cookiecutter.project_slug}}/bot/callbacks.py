"""
Callback query handlers
https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.callbackqueryhandler.html?highlight=CallbackQueryHandler#telegram.ext.CallbackQueryHandler
"""
from telegram import InlineKeyboardMarkup
from telegram.ext import run_async

from . import renderers
from .authentication import authenticate

# Write your callback query handlers here


@run_async
def example_callback_query_handler(update, context):
    query = update.callback_query
    query.answer()

    user = authenticate(update.effective_user)

    text, keyboard = renderers.example_markup(user)
    query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
