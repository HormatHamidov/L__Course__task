from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('dashboard/', dashboard__page, name='dashboard'),
    path('addarticle/', addarticle__page, name='addarticle'),
    path('article/<int:id>', detail__page, name='detail')
    # path('update/', update__page, name='update')
    # path('delete/', delete__page, name='delete')
]