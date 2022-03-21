from django.urls import path
# from .views import movie_list, movie_details, MovieListAV
from .views import WatchListListAV, StreamPlatformListAV, WatchListDetailAV, StreamPlatformDetailAV

urlpatterns = [
    # path('movies/', movie_list),
    # path('movies/<int:pk>/', movie_details),
    path('watchlists/', WatchListListAV.as_view()),
    path('watchlists/<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-detail'),
    path('platforms/', StreamPlatformListAV.as_view()),
    path('platforms/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]