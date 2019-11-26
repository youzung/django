# 함수의 종류
#1. 인자 & 리턴 O
# def sum_ex(a,b):
#     result = a + b
#     return result

# print(sum_ex(2,5))
# sum_result = sum_ex(2,5)
# print(sum_result)
# #2. 리턴만
# def say():
#     return 'hi'
# #3. 인자만
# def say(name, age):
#     print(f'제 이름은 {name}이고, 나이는 {age}입니다.')
# say('juan', 20)
# #4. 인자 & 리턴 X
# def say():
#     print('안녕하세요')

# def say():
#     print('hi')
# say()
# result = say()
# print(result)

# 함수의 인자
#1. 위치 인자(Positional Argument)
'''
def my_func(b,a,c):
    print(f'첫번째는 {a}, 두번째는 {b}, 세번째는 {c}입니다.')
    return a + b + c

result = my_func(1,2,3)
print(result)

#2. 기본값 인자(default argument)
def greeting(name='juan'):
    print(f'{name}님 안녕하세요.')

# greeting()
greeting('bob')

def my_sum(a=2,b):
    return a + b

# print(my_sum(2))
print(my_sum(2,4))

#3. 키워드 인자(Keyword Argument)
def greeting(age, name='juan'):
    print(f'{name}은 {age}살 입니다.')

greeting(19)
greeting(19, 'justin')
greeting(age=22, name='john')
greeting(name='john', age=33)
greeting(name='eric', 19)
greeting(19, name='eric')

# 4. 가변인자
def my_func(*args):
    print(args)
    print(type(args))
    return args

my_func(1,2,3)
my_func(1,2,3,4)
my_func(1,2,3,5,6)

# 5. 정의되지 않은 인자(키워드 인자)
def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_dict(한국어='안녕', 영어='hi', 독일어='Guten tag')

my_dict = {
    '서울':'02'
}
my_dict2 = {}
my_dict2['경기도']='031'

my_dict3 = dict(한국어='안녕', 영어='hi', 독일어='Guten tag')
print(my_dict3)

jumin1 = '900101-1020201'
jumin2 = '910203-2030020'

def male_female(number):
    if number[7] == '1':
        print('남자입니다')
    else:
        print('여자입니다')
male_female(jumin1)
male_female(jumin2)
'''

# 사용자의 입력으로 숫자를 받아서 해당 숫자가 
# 짝수인지 홀수인지 구분하는 함수
# num = int(input('숫자를 입력해주세요: '))
# def even_odd(num):
#     if num % 2:
#         print('홀수입니다')
#     else:
#         print('짝수입니다')
# even_odd(num)

# 리스트 안에서 가장 작은 숫자를 출력하는 함수
items = [1, 2, -5, 0]
def smallest_num(items):
    min_num = items[0]
    for item in items:
        if item < min_num:
            min_num = item
    return min_num
print(smallest_num(items))

# 문자열로만 이루어진 리스트를 인자로 넘겼을때
# 문자열의 길이가 2 이상이고 주어진 문자열의
# 첫번째와 마지막 문자가 같은 문자열의 수를 세는 함수

# def start_end(words):
#     count = 0
#     for word in words:
#         if len(word) >= 2 and word[0] == word[-1]:
#             count += 1
#     return count

# words = ['level','asder','tomato','abdda', 's']
# print(start_end(words))

import requests
from bs4 import BeautifulSoup as bs

# 환율
url = "https://finance.naver.com/marketindex/"

html = requests.get(url).text
soup = bs(html, 'html.parser')
select = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print('지금 원/달러 환율은' + select.text)