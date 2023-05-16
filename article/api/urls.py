from django.urls import path
from .views import (
    ArticleListApiView,
    ArticleDetailApiView,
    ArticleUpdateApiView,
    ArticleDeleteApiView,
    ArticleCreateApiView,
    
    CommentListApiView,
    CommentCreateApiView,
    # CommentDeleteApiView,
    CommentUpdateApiView,
)

app_name = 'articleapi'

urlpatterns = [
    path("list", ArticleListApiView.as_view(), name="list"),
    path("detail/<slug>", ArticleDetailApiView.as_view(), name="detail"),
    path("update/<slug>", ArticleUpdateApiView.as_view(), name="update"),
    path("delete/<slug>", ArticleDeleteApiView.as_view(), name="delete"),
    path("create/", ArticleCreateApiView.as_view(), name="create"),
    # Comment
    path("comment/list", CommentListApiView.as_view(), name="comment_list"),
    path("comment/create/", CommentCreateApiView.as_view(), name="comment_create"),
    # path("comment/delete/<pk>", CommentDeleteApiView.as_view(), name="comment_delete"),
    path("comment/update/<pk>", CommentUpdateApiView.as_view(), name="comment_update"),
]
