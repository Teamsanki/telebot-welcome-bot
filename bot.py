from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import time
import threading
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Bot token from environment variable

# START command handler
def start(update: Update, context: CallbackContext):
    msg = update.message.reply_text(f"👋 Hello {update.effective_user.first_name}, welcome to the bot!")

    # Auto delete the start message after 10 seconds (using thread)
    def delete_after_delay(chat_id, message_id):
        time.sleep(10)
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)

    threading.Thread(target=delete_after_delay, args=(msg.chat_id, msg.message_id)).start()

# NEW MEMBER join handler
def welcome_and_delete(update: Update, context: CallbackContext):
    if update.message.new_chat_members:
        # Delete the join message
        context.bot.delete_message(
            chat_id=update.message.chat.id,
            message_id=update.message.message_id
        )

        # Send custom welcome message
        for user in update.message.new_chat_members:
            context.bot.send_message(
                chat_id=update.message.chat.id,
                text=f"👋 Welcome {user.first_name} to the group!"
            )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command: /start
    dp.add_handler(CommandHandler("start", start))

    # New member join message
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_and_delete))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
