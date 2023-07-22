import telegram

# Telegram bot token
BOT_TOKEN = 'your_bot_token'

# Chat ID to send the message to
CHAT_ID = 'your_chat_id'


def send_telegram_message(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)


# Example usage: Send a message
send_telegram_message('Hello from Python!')
