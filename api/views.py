#django imports
from django.shortcuts import get_object_or_404

#3rd package imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

#app imports
from djJson.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class ReviewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetail(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StreamPlatformListAV(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            platforms = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platforms, context={'request': request})
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            platform.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class WatchListListAV(APIView):
    
    def get(self, request):
        watchlists = WatchList.objects.all()
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
class WatchListDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(watchlist)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(watchlist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            watchlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        
        

# @api_view(['GET', 'POST'])
# def WatchList_list(request):
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors) 
        
#     WatchLists = WatchList.objects.all()
#     serializer = WatchListSerializer(WatchLists, many=True)
#     return Response(serializer.data)


# @api_view(['PUT', 'GET', 'DELETE'])
# def WatchList_details(request, pk):
#     try:
#         WatchList = WatchList.objects.get(pk=pk)
#     except WatchList.DoesNotExist:
#         return Response({"message":"WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#             serializer = WatchListSerializer(WatchList)
#             return Response(serializer.data)
#             return Response(serializer.errors)
    
#     if request.method == 'PUT':  
#         serializer = WatchListSerializer(WatchList, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         WatchList.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


        
    










