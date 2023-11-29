from blog.models import Blog_Post
from django.views.generic import ListView, DetailView
from mailing.models import Mail
from clients.models import Client
from django.conf import settings
from django.core.cache import cache


class BlogPostView(ListView):
    model = Blog_Post
    template_name = 'mailing/home.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.order_by('?')[:3]
        return queryset

    def get_context_data(self, **kwargs):

        if settings.CACHE_ENABLED:
            key = 'mailings'
            cache_data = cache.get(key)
            if cache_data is None:
                mailings = Mail.objects.all()
                cache.set(key, mailings)
            else:
                mailings = Mail.objects.all()
        else:
            mailings = Mail.objects.all()

        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'
        context_data['mailings_quantity'] = str(len(mailings))
        context_data['active_mailings'] = str(len(Mail.objects.filter(status='started')))
        context_data['clients'] = str(len(Client.objects.all()))
        return context_data


class BlogPostDetailView(DetailView):
    model = Blog_Post
    template_name = 'blog/blog_post_detail.html'


class BlogListView(ListView):
    model = Blog_Post
    template_name = 'blog/blog.html'
