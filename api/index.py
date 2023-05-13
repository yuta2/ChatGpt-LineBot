from flask import Flask, request, abort, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from api.chatgpt import ChatGPT
from api.carbon import Carbon
import urllib.parse

import os
import json

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"

app = Flask(__name__)
chatgpt = ChatGPT()

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/carbon')
def test():
    origin_input = '金豐機器工業股份有限公司'
    destination_input = '基隆內港'
    result_text = Carbon.calc_distance(origin_input,destination_input)
    json_data = json.loads(result_text)

    if json_data['status'] == 'OK':
        # distance = json_data['distance']
        # duration = json_data['duration']
        # print(f"距離：{distance} 公尺")
        # print(f"時間：{duration} 秒")
        return json_data
    else:
        return 'no data'

@app.route('/process_data', methods=['POST'])
def process_data():
    # 從POST請求中獲取資料
    body = request.get_data(as_text=True)
    # 處理資料並返回響應
    parsed_data = urllib.parse.parse_qs(body)
    from_value = parsed_data['from'][0]
    to_value = parsed_data['to'][0]
    data = {'from': from_value, 'to': to_value}
    return data
    # return parsed_data


    # 處理資料並返回響應
    # parsed_data = urllib.parse.parse_qs(body)
    # from_value = parsed_data['from'][0]
    # to_value = parsed_data['to'][0]
    # data = {'from': from_value, 'to': to_value}
    # return data

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global working_status
    
    if event.message.type != "text":
        return
    
    if event.message.text == "啟動":
        working_status = True
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="我是時下流行的AI智能，目前可以為您服務囉，歡迎來跟我互動~"))
        return

    if event.message.text == "安靜":
        working_status = False
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="感謝您的使用，若需要我的服務，請跟我說 「啟動」 謝謝~"))
        return

    if working_status:
        chatgpt.add_msg(f"Human:{event.message.text}?\n")
        reply_msg = chatgpt.get_response().replace("AI:", "", 1)
        chatgpt.add_msg(f"AI:{reply_msg}\n")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run()
