from django.shortcuts import render, redirect
from .models import Student

def index(request):
    # articles = Article.objects.all()
    # articles = Article.objects.order_by('-pk')
    # students = Student.objects.all()[::-1]
    students = Student.objects.order_by('pk')
    
    return render(request, 'students/index.html', {'students': students})

def new(request):
    return render(request, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    student = Student(name=name, email=email, age=age)
    student.save()

    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    # article = Article(title=title, content=content)
    # article.save() 

    # 3.
    # Article.objects.create(title=title, content=content)
    
    #return render(request, 'articles/create.html')
    return redirect(f'/students/{student.pk}/')


def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/detail.html', {'student': student})

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')

def edit(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/edit.html', {'student': student})

def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.age = request.POST.get('age')
    student.save()
    return redirect(f'/students/{student.pk}')
