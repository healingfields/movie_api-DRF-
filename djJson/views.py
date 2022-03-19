from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from .models import WatchList
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.
def watchlist_list(request):
    watchlists = WatchList.objects.all()
    return JsonResponse(list(watchlists.values()), safe=False)

def watchlist_details(request, pk):
    try:
        watchlist = get_object_or_404(WatchList, pk=pk)
        watchlist_dict = {
            'name': WatchList.name,
            'description': WatchList.storyline,
            'active': WatchList.active
        }
        return JsonResponse(watchlist_dict)
    except WatchList.DoesNotExist:
        return HttpResponseNotFound







