class Person:
    name = '아이유'

    def say_hello(self):
        print(f'hello! {self.name}')

# 클래스 -> 인스턴스
iu = Person()
# 인스턴스를 통해 메서드를 호출
iu.say_hello()
# 인스턴스를 통해 속성에 접근
print(iu.name)
# 클래스를 통해 속성에 접근
print(Person.name)
# 클래스를 통해 메서드 호출
Person.say_hello(iu)

iu.name = 'momo'
# print(iu.name)
print(Person.name)

class Person:
    name = '아이유'
    age = '19'

    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 제 나이는 {self.age}살 입니다.')

iu = Person()
iu.greeting()

print(iu.name)
print(iu.age)


name = '?'

class Person:
    name = '홍길동'

    def greeting(self):
        print(f'{name}')

p1 = Person()
# print(p1.name)
# print(Person.name)

# p1.name = '아이유'
# print(p1.name)
# print(Person.name)

word = "Not class member"

class Something:
    word = "Class member"

    def Set(self, msg):
        self.word = msg
    def Print(self):
        print(word)

g = Something()
g.Set('First Message')
g.Print()

class Person:
    name = 'kang'
    def __init__(self, name):   # 생성자 메서드 -> 인스턴스 객체를 생성할 때 자동으로 생성자 메서드가 호출됩니다.
        print(f'하이 {name}')
    def greeting(self):
        print(f'{self.name}입니다. 만나서 반갑습니다.')
    def __del__(self):  # 소멸자 메서드 -> 객체의 참조 카운터가 0이 되면 자동으로 소멸자 메서드가 호출됩니다.
        print('바이')
hong = Person('hong')
hong.greeting()
hong.greeting()


class Myclass:
    name = '홍길동'
    def __init__(self, value): #4. self = d, value = 10
        self.value = value  #5. self.value -> d.value = 10
        print(f'{self.value}가 생성되었습니다.')  #6. self.value -> d.value -> 10
    def __del__(self):
        print('소멸되었습니다.') #7. 소멸

def foo():  #2. foo 함수 실행
    d = Myclass(10)  #3. d라는 인스턴스
foo()   #1. 함수 호출


class Person:
    name='juan'

p1 = Person()
p2 = Person()

# print(p1.name)
# print(p2.name)
# print(Person.name)
# p1.name = 'eric'
# print(p1.name)
# print(p2.name)
# print(Person.name)
# Person.title = "Welcome"
# print(p1.title)
# print(p2.title)
# print(Person.title)
# p1.water = '삼다수'
# print(p1.water)
# # print(p2.water)
# print(Person.water)

class Person:
    population = 0 # 클래스 변수 -> 모든 인스턴스를 공유

    def __init__(self,name):    # 생성자 함수(매직 메서드) -> 인스턴스 생성시에 호출이 된다
        self.name = name    # me.name = name(juan), name -> 인스턴스 별로 각각 가지는 변수
        Person.population += 1

    def greeting(self):
        print(f'{self.name}입니다. 만나서 반갑습니다.')

me = Person('juan')
print(me.name)

friend = Person('bob')
print(friend.name)

print(Person.population)
print(me.population)
print(friend.population)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'안녕하세요, 저는 {self.name}입니다.')

class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 제 학번은 {self.student_id}입니다.')

# s1 = Person('juan')
# s1.greeting()
# s2 = Student('justin', 12345)
# s2.greeting()