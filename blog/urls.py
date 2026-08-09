from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('search/',blog_search,name='search'),
    path('post/<int:pid>/',blog_single_view,name='single'),
    path('category/<str:cid>/', blog_view, name='category'),
    path('author/<str:author_username>/', blog_view, name='author'),
]