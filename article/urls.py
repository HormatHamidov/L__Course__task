from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('', articles__page, name='articles'),
    path('dashboard/', dashboard__page, name='dashboard'),
    path('addarticle/', addarticle__page, name='addarticle'),
    path('article/<int:id>', detail__page, name='detail'),
    path('comment/<int:id>', comment__page, name='comment'),
    path('update/<int:id>', update__page, name='update'),
    path('delete/<int:id>', delete__page, name='delete')
]