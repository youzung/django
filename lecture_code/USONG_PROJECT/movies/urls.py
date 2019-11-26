from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_id>/score/<int:score_id>/delete', views.score_delete, name='score_delete'),
    path('<int:movie_id>/score/new', views.score_new, name='score_new'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]