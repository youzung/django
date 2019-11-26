from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles':articles})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 사용자가 ArticleForm 으로 보낸 데이터를 받아서 form이라는 인스턴스를 생성
        # form 의 type은 ArticleForm 이라는 클래스의 인스턴스(request.POST는 QueryDict로 담긴다.)
        if form.is_valid(): # form이 유효한지 체크한다
            article = form.save()
            # form.cleaned_data 데이터를 요청받은대로 처리한다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail',article.id)
    else:
        form = ArticleForm()
        # 상황에 따라 context에 넘어가는 2가지 form
        # 1. GET : 기본 form 으로 넘겨짐
        # 2. POST : 검증에 실패(is_valid -> False)한 form(오류 메시지를 포함한 상태)로 넘겨짐
    return render(request, 'articles/form.html', {'form':form})

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:index')
    # else:
    #     return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.order_by('-pk')
    comment_form = CommentForm()
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments, 'comment_form':comment_form})

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
        # form = ArticleForm(initial={'title':article.title, 'content':article.content})
        # form = ArticleForm(initial=article.__dict__)  # 딕셔너리 자료형이 되어 저장
    return render(request, 'articles/form.html', {'form':form, 'article':article})

def comment_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            # content = comment_form.cleaned_data.get('content')
            # comment = Comment.objects.create(content=content, article=article)
        # comment = Comment()
        # comment.content = request.POST.get('content')
        # comment.article = article
        # comment.save()
    return redirect('articles:detail', article_id)

def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
    return redirect('articles:detail', article_id)

    