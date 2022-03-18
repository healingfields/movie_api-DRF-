from django.urls import path
# from .views import movie_list, movie_details, MovieListAV
from .views import MovieListAV, MovieDetailAV

urlpatterns = [
    # path('movies/', movie_list),
    # path('movies/<int:pk>/', movie_details),
    path('movies/', MovieListAV.as_view()),
    path('movies/<int:pk>/', MovieDetailAV.as_view()),
    
]