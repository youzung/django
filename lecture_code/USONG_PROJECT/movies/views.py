from django.shortcuts import render, redirect
from .models import Movie, Score
from .models import Genre

def index(request):
    # articles = Article.objects.all()
    # articles = Article.objects.order_by('-pk')
    movies = Movie.objects.all()[::-1]
    return render(request, 'movies/index.html', {'movies': movies})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
        movie.save()
        
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/new.html')

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    scores = movie.score_set.order_by('-pk')
    return render(request, 'movies/detail.html', {'movie': movie, 'scores': scores})

def delete(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else: 
        return recirect('movies:detail', movie.pk)

def update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/edit.html', {'movie': movie})

def score_new(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == "POST":
        score = Score()
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.movie_id = movie
        score.save()
    return redirect('movies:detail', movie_id)

def score_delete(request, movie_id, score_id):
    if request.method == "POST":
        score = Score.objects.get(pk=score_id)
        score.delete()
    return redirect('movies:detail', movie_id)