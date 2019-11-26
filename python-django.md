### 기본

```bash
source ./venv/Scripts/activate
cd DJANGO_BLOG
python manage.py runserver
```



### 프로젝트 생성

```bash
django-admin startproject [프로젝트명]
cd [프로젝트명]
django-admin startapp [프로젝트 내부 앱(새로운 이름)]
```



### 1. 프로젝트 내부의 models.py 수정

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        #return f'{self.id}번 글 - {self.title} : {self.content}'
        return f'{self.name} 학생'
```



### 2. DB테이블 생성

```bash
python manage.py makemigrations
python manage.py migrate
```



### 3. 관리자 설정

```bash
python manage.py createsuperuser
```



### pip install 

- django-bootstrap4
- django-imagekit
- Pillow
- pilkit
- faker



shift + tab

tab