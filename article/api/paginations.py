from rest_framework.pagination import PageNumberPagination

class ArticlePagination(PageNumberPagination):
    page_size = 2
    
    
class CommentPagination(PageNumberPagination):
    page_size = 2