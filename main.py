import telebot
import json
import sys


with open('credentials.json', 'r') as credentials_json:
    credentials = json.load(credentials_json)

TOKEN = credentials.get('bot_api_token')

bot = telebot.TeleBot(TOKEN)


def sent_build():
    project_name = sys.argv[1]
    file_name = sys.argv[2]

    project_credentials = credentials.get('projects').get(sys.argv[1])

    chat_id = project_credentials.get('chat_id')
    builds_path = project_credentials.get('builds_path')

    bot.send_message(chat_id, f'Привет, у меня есть новый билд проекта {project_name}')

    with open(builds_path + file_name, 'rb') as build:
        bot.send_document(chat_id, build)


if __name__ == '__main__':
    sent_build()
