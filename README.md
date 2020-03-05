This tg bot created for sending builds to tg chanel

For start you must:

1. pip install -r requirements.txt
2. create file credentials.json. This file must have this tree structure:
{
  "bot_api_token": your telegram bot token (give it in BotFather @BotFather),
  "projects": {
    "Project1": {
      "chat_id": your chat_id,
      "builds_path": path to dir where are your builds 
    },
    "Project2": {
      "chat_id": your chat_id,
      "builds_path": path to dir where are your builds 
    },
   ...
    "ProjectN": {
      "chat_id": your chat_id,
      "builds_path": path to dir where are your builds 
    },
  }
}

you can get your tg chat_id used get_chat_id.py
 2.1 add bot to your chat
 2.2 run get_chat_id.py
 2.3 write /start in your chat
 
3. run main script used "py main.py YourProjectName YourFileName"
