from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin #UpdateModelMixin,RetrieveModelMixin

from article.models import Article,Comment
from .serializers import ArticleSerializer,CommentSerializer

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import ArticlePagination,CommentPagination

class ArticleListApiView(ListAPIView,CreateModelMixin):
    queryset = Article.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    # def get_queryset(self):
    #     queryset = Article.objects.filter(article_image = False)


class ArticleDetailApiView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArticleDeleteApiView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArticleUpdateApiView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"


class ArticleCreateApiView(CreateAPIView,ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


################################ Comment ############################################
class CommentListApiView(ListAPIView):
    queryset = Comment.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    
    
class CommentCreateApiView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



# Update-de Delete elediyimiz ucun artiq bu view-a gerek yoxdur.

# class CommentDeleteApiView(DestroyAPIView): #UpdateModelMixin, RetrieveModelMixin bunlar import edilir ilk once
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = "pk"
    
    # def put(self,request,*args,**kwargs): Delete zamani update ede bilmek ucun
    #     return self.update(request,*args,**kwargs)

    # def get(self,request,*args,**kwargs):    Update ederken icinde datalarmizinda gelmeyi
    #     return self.retrieve(request,*args,**kwargs)

class CommentUpdateApiView(RetrieveUpdateAPIView,DestroyModelMixin): #Update zamani delete-de ede bilmek ucun
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)