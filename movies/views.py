from django.shortcuts import render,redirect
from django.views.decorators.http import require_safe

from .models import Movie
from .forms import MovieForm

from django.http.response import JsonResponse,HttpResponse
from django.core import serializers



# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request,'movies/index.html',context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movei':movie
    }
    return render(request,'movies/detail.html',context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        return render(request,'movies/recommended.html')
    
    
def latest_movie(request):
    # movies = Movie.objects.filter(release_date=)
    movies = Movie.objects.order_by('-release_date')[:10]
    data = serializers.serialize('json',movies)
    return HttpResponse(data, content_type='application/json')      

def great_movie(request):
    movies = Movie.objects.filter(vote_average__gte=8.6) 
    data = serializers.serialize('json',movies)
    return HttpResponse(data, content_type='application/json')    

def popular_movie(request):
    movies = Movie.objects.filter(popularity__gte=40.0) 
    data = serializers.serialize('json',movies)
    return HttpResponse(data, content_type='application/json')    
