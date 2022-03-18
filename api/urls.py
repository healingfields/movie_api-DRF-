from django.urls import path
from .views import movie_list, movie_details

urlpatterns = [
    path('movies/', movie_list),
    path('movies/<int:pk>/', movie_details),
]