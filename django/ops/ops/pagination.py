from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'
    page_size = 5
