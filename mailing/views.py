from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailing.models import Mail, Message
from mailing.forms import MailingForm, MessageForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MailingListVeiw(ListView):
    model = Mail
    template_name = 'mailing/mail_list.html'
    extra_context = {'title': 'Список рассылок'}


class MailCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')

    def form_valid(self, form):
        if form.is_valid():
            mailing = form.save()
            mailing.user_id = self.request.user
            mailing.save()

        return super().form_valid(form)


class MailDetailView(DetailView):
    model = Mail


class MailUpdateView(LoginRequiredMixin, UpdateView):
    model = Mail
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')
    template_name = 'mailing/mail_update_form.html'



class MailDeleteView(LoginRequiredMixin, DeleteView):
    model = Mail
    success_url = reverse_lazy('mailing:home')
