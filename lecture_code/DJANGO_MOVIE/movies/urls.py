from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/score/<int:score_pk>/delete/', views.score_delete, name='score_delete'),
    path('<int:movie_pk>/score/new/', views.score_new, name='score_new'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
