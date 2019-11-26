from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 사용자가 ArticleForm 으로 보낸 데이터를 받아서 form이라는 인스턴스를 생성
        # form 의 type은 ArticleForm 이라는 클래스의 인스턴스(request.POST는 QueryDict로 담긴다.)
        if form.is_valid(): # form이 유효한지 체크한다.
            article = form.save()
            # form.cleaned_date 데이터를 요청받은대로 처리한다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:index')
    else:
        form = ArticleForm()
            # 상황에 따라 context에 넘어가는 2가지 form
            # 1. GET : 기본 form 으로 넘겨짐
            # 2. POST : 검증에 실패(is_valid -> False)한 form(오류 메시지를 포함)

            # return render(request, 'articles/new.html')
    return render(request, 'articles/form.html', {'form': form})
    #else:
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:index')

    #    return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    return render(request, 'articles/detail.html', {'article': article})

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            return redirect('articles:detail', article.pk)
    else: 
        # ArticleForm 을 초기화(이전에 DB에 저장된 데이터 입력값을 넣어준 상태)
        form = ArticleForm(instance=article)
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        # form = ArticleForm(initial=article.__dict__) # 딕셔너리 자료형
    return render(request, 'articles/form.html', {'form': form, 'article': article})
