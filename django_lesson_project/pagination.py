from rest_framework import pagination


class DjangoLessonPaginationClass(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 1000
    page_size_query_param = "size"
