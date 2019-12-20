from flask import Flask, render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

app_url = f"https://api.telegram.org/bot{token}"

@app.route('/')
def hello():
    return "안녕하세요!"

@app.route('/write')
def write():
    #html file
    return render_template("write.html")

@app.route('/send')
def send():
    message = request.args.get("message")
    message_url = app_url + f"/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(message_url)
    return "메시지 전송 완료했어요!" 

#Webhook
@app.route(f"/{token}", methods=['POST'])
def telegram():
    #setwebhook
    #https://api.telegram.org/bot955008193:AAGHDaJE41mkARQsYrRlcsm2pja8hbEnIVQ/setWebhook?url=https://8322ba72.ngrok.io/955008193:AAGHDaJE41mkARQsYrRlcsm2pja8hbEnIVQ
    #print(request.get_json())
    # 실습 1 : 사용자의 아이디랑 텍스트 
    # 앵무새
    # 실습 2 : 텔레그램 메세지 보내기 요청 

    response = request.get_json()
    print(response)
    chat_id = response["message"]["from"]["id"]
    text = response["message"]["text"]
    print(chat_id)
    print(text)
    #message = request.args.get(text)
    
    result = []

    if text == "/로또":
        # 숫자 6개
        [result.append(sorted(random.sample(range(1,46), 6))) for _ in range(5)]
        text = result
    elif text == "/점심":
        #점심 메뉴 추천
        menus = ["20층", "양자강", "맥도날드","바스버거"]
        text = random.choice(menus)

    message_url = app_url + f"/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(message_url)
    #return body, status_code 

    return '', 200 #응답성공


#debug 
if __name__ == "__main__":
    app.run(debug=True)

