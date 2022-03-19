from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.watchlist_list),
    path('movies/<int:pk>/', views.watchlist_details),
]