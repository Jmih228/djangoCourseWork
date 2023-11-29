from django.urls import path
from django.views.decorators.cache import cache_page
from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='blog_post_detail_view'),
    path('', cache_page(600)(BlogListView.as_view()), name='blog')
]