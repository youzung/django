from django.contrib import admin
from .models import Movie
from .models import Genre
from .models import Score

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id')

admin.site.register(Movie, MovieAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'score', 'movie_id')

admin.site.register(Score, ScoreAdmin)

