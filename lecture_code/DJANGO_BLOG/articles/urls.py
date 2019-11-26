from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<int:article_id>/follow/<int:user_id>/', views.follow, name='follow'),
    path('<int:article_id>/like/', views.like, name='like'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:article_id>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/update/', views.update, name='update'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    # path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]