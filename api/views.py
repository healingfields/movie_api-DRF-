# django imports
from django.shortcuts import get_object_or_404

# 3rd package imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle
from rest_framework import filters

# app imports
from djJson.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .permissions import IsReviewUserOrReadOnly, IsAdminOrReadOnly
from .throttling import ReviewListThrottle, ReviewCreateThrottle
from django_filters.rest_framework import  DjangoFilterBackend


class ReviewCreateByWatchlist(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, user=user)

        if review_queryset.exists():
            raise ValidationError("this user already reviewed this movie")

        if watchlist.nbr_reviews == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2

        watchlist.nbr_reviews += 1
        watchlist.save()
        serializer.save(watchlist=watchlist, user=user)


class ReviewListByWatchlist(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewUserOrReadOnly]
    throttle_classes = [UserRateThrottle]

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)


class StreamPlatformListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'platform-list'

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
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [IsAdminOrReadOnly]

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


class UserReviewByUsername(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Review.objects.filter(user__username=username)


class UserReviewByQuery(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__username', 'active']

    # def get_queryset(self):
    #     username = self.request.query_params.get('username', None)
    #     return Review.objects.filter(user__username=username)

class MoviesBySearch(generics.ListAPIView):
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()
    filter_backends = [filters.SearchFilter]



# @api_view(['GET', 'POST'])
# def WatchList_list(request):
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
