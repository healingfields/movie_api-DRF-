from django.urls import path
# from .views import movie_list, movie_details, MovieListAV
from .views import WatchListListAV, StreamPlatformListAV, WatchListDetailAV, StreamPlatformDetailAV, ReviewListByWatchlist, ReviewDetail, ReviewCreateByWatchlist, UserReviewByQuery, UserReviewByUsername, MoviesBySearch, WatchList


urlpatterns = [
    # path('movies/', movie_list),
    # path('movies/<int:pk>/', movie_details),
    path('watchlists/', WatchList.as_view()),
    path('watchlists/<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-detail'),
    path('platforms/', StreamPlatformListAV.as_view()),
    path('platforms/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    path('<int:pk>/review-create/', ReviewCreateByWatchlist.as_view()),
    path('<int:pk>/review/', ReviewListByWatchlist.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('<str:username>/reviews/', UserReviewByUsername.as_view(), name='user-reviews'),
    path('reviews/', UserReviewByQuery.as_view(), name='user-reviews'),
    path('movies/', MoviesBySearch.as_view(), name='movies-search')


]