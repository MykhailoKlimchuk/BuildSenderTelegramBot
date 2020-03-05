import telebot
import json


with open('credentials.json', 'r') as credentials_json:
    credentials = json.load(credentials_json)

TOKEN = credentials.get('bot_api_token')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def button_click(message):
    response_message = f'Привет, я создан для отправки новых билдов'
    print(message.chat.id)
    bot.send_message(message.chat.id, response_message)

bot.polling()
