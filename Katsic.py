import os
import requests
import telebot
from telegram.ext import Updater, CommandHandler, MessageHandler

# Meta AI API settings
api_key = os.environ.get("META_API")
api_endpoint = "(link unavailable)"

# Telegram Bot settings
telegram_token = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Hello! I'm Royal Katsic, your AI assistant.")

def handle_message(update, context):
    message = update.message.text
    response = meta_ai_generate_response(message)
    update.message.reply_text(response)

def meta_ai_generate_response(input_text):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"input": input_text}
    try:
        response = requests.post(api_endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["output"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    updater = Updater(telegram_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
