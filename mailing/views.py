from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailing.models import Mail, Message
from mailing.forms import MailingForm, MessageForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin



class MailingListVeiw(ListView):
    model = Mail
    template_name = 'mailing/mail_list.html'
    extra_context = {'title': 'Список рассылок'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset


class MailCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailingForm
    success_url = reverse_lazy('mailing:message_create')

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
    success_url = reverse_lazy('mailing:mailings')
    template_name = 'mailing/mail_update_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Mail, Message, form=MessageForm, extra=0)
        context_data['formset'] = MessageFormset()
        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)



class MailDeleteView(LoginRequiredMixin, DeleteView):
    model = Mail
    success_url = reverse_lazy('mailing:mailings')

def change_status(request, pk):

    mail = get_object_or_404(Mail, pk=pk)
    print(mail.status)
    if mail.status != 'blocked':
        mail.status = 'blocked'
        print(mail.status)
    else:
        mail.status = 'created'
    mail.save()
    return redirect(reverse('mailing:mailings'))


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:mailings')

    def form_valid(self, form):
        if form.is_valid():
            mailing = Mail.objects.filter(user_id=self.request.user.id).order_by('-creation_date')[0]
            print(form)
            message = form.save()
            message.mail_id = mailing.id
            message.save()

        return super().form_valid(form)
