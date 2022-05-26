#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, \
TextSendMessage, ImageSendMessage, StickerSendMessage

line_bot_api = LineBotApi('XDmqIy6qdVPR/19EazltAxqqXpkh+2I2qC1Tu1xmtfsCX/hTqWr3DiHGJ2yeUPL2onV66YdqPemJQQwAbAv5a8UdukXpIeP45VteKbYA/l4Pun4ZFgqNqZLtTEZikzG3ysngNmI6ERnERVpopoL8PwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('554774a8660b2f383efdda8d344d4cae')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line_signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InbalidSignatureError:
        abort(400)
    return 'OK'

@app.route("/")
def test():
    return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

@handler.add(MessageEvent)
def handle_message(event):
    ms_type = event.message.type

    if ms_type == 'text':
        reply = TextSendMessage(text=event.message.text)
    elif ms_type == 'image':
        image_url = 'https://romanakchurin.com/favicon.ico'
        reply = ImageSendMessage(original_content_url=image_url,
            preview_image_url=image_url)
    elif ms_type == 'sticker':
        reply = StickerSendMessage(package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    line_bot_api.reply_message(event.reply_token, reply)

if __name__ == "__main__":
    app.run()



# token
# XDmqIy6qdVPR/19EazltAxqqXpkh+2I2qC1Tu1xmtfsCX/hTqWr3DiHGJ2yeUPL2onV66YdqPemJQQwAbAv5a8UdukXpIeP45VteKbYA/l4Pun4ZFgqNqZLtTEZikzG3ysngNmI6ERnERVpopoL8PwdB04t89/1O/w1cDnyilFU=

# secret
# 554774a8660b2f383efdda8d344d4cae

# channel_id
# 1656300945

# pip install line-bot-sdk==1.18.0
# ngrok.exe ngrok http 5000