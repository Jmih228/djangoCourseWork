from django.urls import path
from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='blog_post_detail_view'),
]