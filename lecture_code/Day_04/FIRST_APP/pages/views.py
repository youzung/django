from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
import random
import datetime

def index(request):
    return render(request, 'pages/index.html')

def match(request):
    chemi = random.randint(50, 100)
    me = request.POST.get('me')
    you = request.POST.get('you')
    test = request.method
    context = {
        'me':me,
        'you':you,
        'chemi':chemi,
        'test':test,
    }
    return render(request, 'pages/match.html', context)

def home(request):
    name = 'juan'
    data = ['A','B','C']
    empty_data = ['엄복동', '클레멘타인', '성냥팔이소녀의 재림']
    matrix = [[1,2,3],[4,5,6]]
    context = {
        'name':name,
        'data':data,
        'empty_data':empty_data,
        'matrix':matrix,
        'number':10,
        'datetime':datetime,
    }
    return render(request, 'pages/home.html', context)

def lotto(request):
    lotto = sorted(random.sample(range(1,46),6))
    return render(request, 'pages/lotto.html', {'lotto':lotto})

def cube(request, num):
    cube = num ** 3
    context = {
        'cube':cube,
        'num':num,
    }
    return render(request, 'pages/cube.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')

def dtl(request):
    my_list = ['짜장면', '짬뽕','탕수육','양장피']
    messages = ['apple','banana','mango','watermelon','kiwi']
    empty_list = []
    context = {
        'my_list':my_list,
        'messages':messages,
        'empty_list':empty_list,
    }
    return render(request, 'pages/dtl.html', context)

def kospi(request):
    url = 'https://finance.naver.com/sise/'
    res = requests.get(url).text
    soup = bs(res, 'html.parser')
    kospi = soup.select_one('#KOSPI_now')
    return render(request, 'pages/kospi.html', {'kospi':kospi.text})