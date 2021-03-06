from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchlistPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'pg'
    max_page_size = 4
    page_size_query_param = 'size'
    last_page_strings = ['end']


class MoviesLOPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'size'
    offset_query_param = 'start'
    max_limit = 4


class MoviesCursorPagination(CursorPagination):
    page_size = 2
    cursor_query_param = 'record'
    ordering = '-created'
