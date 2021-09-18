"""
Write your conversation handlers here:
- Conversation entry points
    - Callback query handlers
    - Command handlers
- Conversation states
"""

from telegram.ext import run_async, ConversationHandler

# Write your conversation entry points (callback query handlers here)


# Example: handle input of user's feedback
@run_async
def input_feedback(update, context):

    # Do something with the user feedback. Maybe storing it and send it to the bot admins?

    return ConversationHandler.END
