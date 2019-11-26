from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Score(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete = models.CASCADE)

    def __str__(self):
        return f'<Score({self.id}) : content({self.content}), score({self.score}), movie_id({self.movie_id})>'
