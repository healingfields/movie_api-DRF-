from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from .models import Movie
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return JsonResponse(list(movies.values()), safe=False)

def movie_details(request, pk):
    try:
        movie = get_object_or_404(Movie, pk=pk)
        movie_dict = {
            'name': movie.name,
            'description': movie.description,
            'active': movie.active
        }
        return JsonResponse(movie_dict)
    except Movie.DoesNotExist:
        return HttpResponseNotFound







