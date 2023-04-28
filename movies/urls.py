from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    path('latest/',views.latest_movie, name='latest_movie'),
    path('great/',views.great_movie, name='great_movie'),
    path('popular/',views.popular_movie, name='popular_movie')
]
