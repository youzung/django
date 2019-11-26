from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/sparta')
def sparta():
    return "This is sparta"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다! {name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num**3 # num*num*num
    return f'{num}의 세제곱은 {result}입니다.'

@app.route("/dinner/<int:person>")
def dinner(person):
    menu = ['짜장면','짬뽕','볶음밥','고추잡채밥','마파두부밥']
    order = random.sample(menu, k=person)
    return str(order)

@app.route("/lotto")
def lotto():
    nums = range(1,46)
    lotto = random.sample(nums, k=6)
    return str(lotto)

@app.route("/html")
def html():
    return "<h1> This is HTML h1 tag! </h1>"

@app.route("/d_day")
def d_day():
    today = datetime.now()
    finish = datetime(2019,11,27)
    remain = finish - today
    return f'우리가 같이 있을 수 있는 시간이 이제 {remain}일 밖에 안남았어..ㅠㅠ'

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route('/myday')
def myday():
    today = datetime.now()
    return render_template('myday.html', today=today)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('pong.html', name=name, age=age)

@app.route('/name')
def name():
    return render_template('name.html')

@app.route('/god')
def god():
    name = request.args.get('name')
    source = ['냉정','열정','잘생김','못생김','매력','시크','섹시']
    style = random.sample(source, 3)
    return render_template('god.html', name=name, style=style)