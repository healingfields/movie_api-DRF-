#django imports
from django.shortcuts import get_object_or_404

#3rd package imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#app imports
from djJson.models import Movie
from .serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors) 
        
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'GET', 'DELETE'])
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"message":"movie not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
            return Response(serializer.errors)
    
    if request.method == 'PUT':  
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
    










