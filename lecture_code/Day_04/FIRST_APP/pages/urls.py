from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index),
    path('match/', views.match),
    path('home/', views.home),
    path('lotto/', views.lotto),
    path('cube/<int:num>/', views.cube),
    path('static_example/', views.static_example),
    path('dtl/', views.dtl),
    path('kospi/', views.kospi),
]