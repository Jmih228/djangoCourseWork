from blog.models import Blog_Post
from django.views.generic import ListView, DetailView
from mailing.models import Mail
from clients.models import Client


class BlogPostView(ListView):
    model = Blog_Post
    template_name = 'mailing/home.html'


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.order_by('?')[:2]
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Главная'
        context_data['mailings_quantity'] = str(len(Mail.objects.all()))
        context_data['active_mailings'] = str(len(Mail.objects.filter(status='started')))
        context_data['clients'] = str(len(Client.objects.all()))
        return context_data


class BlogPostDetailView(DetailView):
    model = Blog_Post
    template_name = 'blog/blog_post_detail.html'
