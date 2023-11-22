import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open("info.json", "r")
info = json.load(file)

CHANNEL_ACCES_TOKEN = info["CHANNEL_ACCES_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCES_TOKEN)

def main():
      USER_ID = info["USER_ID"]
      messages = TextSendMessage(text = "おはようございます！\n先輩！")
      line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
      main()