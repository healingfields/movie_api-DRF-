from rest_framework.pagination import PageNumberPagination


class WatchlistPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'pg'
    max_page_size = 4
    page_size_query_param = 'size'
    last_page_strings = ['end']
