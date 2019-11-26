from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        #return f'{self.id}번 글 - {self.title} : {self.content}'
        return f'{self.name} 학생'