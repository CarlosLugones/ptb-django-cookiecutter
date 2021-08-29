"""
A renderer returns a tuple of (text, keyboard) which is sent to the user.
I advice you to follow this structure.
"""

from telegram import InlineKeyboardButton

# Write your renderers here


# Example:
def example_markup(user):

    text = 'Example text'

    keyboard = [
        [InlineKeyboardButton(text='Example button', url='https://lugodev.com')]
    ]

    return text, keyboard
