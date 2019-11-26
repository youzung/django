from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint as pp
import random
app = Flask(__name__)

base = "https://api.telegram.org"
token = config('TOKEN')

@app.route('/')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # chat_id를 가져오는 코드
    #1. getUpdates 메소드로 요청보내기
    method = 'getUpdates'

    url = f'{base}/bot{token}/{method}'
    res = requests.get(url).json()
    # pp(res)

    #2. 받아온 응답(json)을 dictionary로 바꿔서 첫번째 메시지의 chat_id를 가져온다
    chat_id = res['result'][0]['message']['chat']['id']

    #3. write.html에서 보내온 msg를 받아 telegram api를 통해 메시지 전송
    method = 'sendMessage'
    text = request.args.get('msg')
    url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'

    requests.get(url)
    return '전송완료'

@app.route(f'/{token}', methods=['POST'])
def webhook():
    #1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서
    url = f'{base}/bot{token}/setWebhook?url=https://7df8ca78.ngrok.io/{token}'
    # https://api.telegram.org/bot810810149:AAHxEydh7DeiqdVlIr1kBmszimG64ng1D24/setWebhook?url=https://7df8ca78.ngrok.io/810810149:AAHxEydh7DeiqdVlIr1kBmszimG64ng1D24
    requests.get(url)
    #2. 그대로 전송
    res = request.get_json()

    if res.get('message'):
        text = res.get('message').get('text')
        if text == '로또':
            text = str(sorted(random.sample(range(1,46),6)))
        elif text[0:4] == '/번역 ':
            naver_client_id = config('NAVER_CLIENT_ID')
            naver_client_secret = config('NAVER_CLIENT_SECRET')

            url = 'https://openapi.naver.com/v1/papago/n2mt'
            text = text[4:]
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {
                'source' : 'ko',
                'target' : 'en',
                'text' : text
            }
            response = requests.post(url, data=data, headers=headers).json()
            text = response.get('message').get('result').get('translatedText')
        

        chat_id = res.get('message').get('chat').get('id')
        method = 'sendMessage'
        url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
        requests.get(url)
    return '', 200

