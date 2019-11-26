from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint as pp

def index(request):
    return render(request, 'utilities/index.html')

def papago(request):
    return render(request, 'utilities/papago.html')

def translated(request):
    # 1. 사용자가 입력한 번역을 하고싶은 한국어 텍스트
    korean = request.GET.get('text')

    # 2. 네이버에 (POST) 번역 요청을 위해서 필요한 내용
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    # 3. 요청을 보낼 url
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    # 4. 헤더 정보 구성
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret,
    }

    # 5. 우리가 요청할 데이터
    data = {
        "source": "ko",
        "target": "en",
        "text": korean,
    }
    
    # 6. 네이버로 요청보내기
    papago_response = requests.post(
        papago_url, headers=headers, data=data
    ).json() 
    # .json()을 통해서 요청의 결과를 dict로 변환한다.
    pp(papago_response)

    # 7. 응답 결과
    english = papago_response['message']['result']['translatedText']

    context = {'korean':korean, 'english':english}
    return render(request, 'utilities/translated.html', context)