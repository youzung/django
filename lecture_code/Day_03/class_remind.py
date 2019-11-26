class Person:
    name = '홍길동'
    age = 19
    hometown = 'Seoul'
    movie = 'action'
    hobby = 'exercise'

    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}이고 나이는 {self.age}살입니다. {self.hometown}태생이고, {self.movie}영화 좋아하고, {self.hobby}을(를) 즐겨합니다. 잘부탁드립니다.')

hong = Person()
kang = Person()
hong.greeting()
kang.name = '강동주'
kang.age = 25
Person.greeting(kang)

print(hong.name)
print(kang.name)
print(Person.name)
hong.name = '홍진영'
print(hong.name)
print(hong.age)
print(kang.name)
print(kang.age)
print(Person.name)

Person.title = 'Welcome'
print(hong.title)
print(kang.title)
print(Person.title)
print(hong.hobby)
print(kang.movie)
print(Person.hometown)

hong.water = '삼다수'
print(hong.water)
print(kang.water)
print(Person.water)

class Teacher:
    def __init__(self, student):
        self.student = student
    
    def shouting(self):
        print(f'{self.student}님, 지각이시네요')

class Student:
    def __init__(self, teacher):
        self.teacher = teacher
    
    def responding(self):
        print(f'{self.teacher}강사님, 내일은 일찍 올께요.')

t1 = Teacher('윤현수')
s1 = Student('변승환')
t1.shouting()
s1.responding()    

class Person:
    name = 'han'
    age = 27
    def __init__(self,name):
        self.name = name
    def greeting(self):
        print(f'안녕하세요, 저는 {self.name}입니다.')

class Student(Person):
    name = 'chris'
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 제 학번은 {self.student_id}입니다.')

p1 = Person('juan')
p1.greeting()
p2 = Student('justin', 12345)
p2.greeting()
print(Student.name)
print(Student.age)
print(p2.name)
print(p2.student_id)
p3 = Student('eric') # error
p3.greeting()