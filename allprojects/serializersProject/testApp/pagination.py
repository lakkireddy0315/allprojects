from rest_framework.pagination import PageNumberPagination,CursorPagination


class MyPagination(PageNumberPagination):
    page_size=7
    page_query_param='mypage'
    page_size_query_param='num'
    max_page_size=11
    last_page_strings=('end_page',)

class MyPagination3(CursorPagination):
     #based on descending order of employee salaries
    page_size=5
    cursor_query_param='mycursor'
    ordering = '-esal'
