from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size= 4
    

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 2
    
class WatchListCursorPagination(CursorPagination):
    page_size = 4
    ordering = '-created'