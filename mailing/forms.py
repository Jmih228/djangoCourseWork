from django import forms
from mailing.models import Mail, Message


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mail
        exclude = ('user', 'status',)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('mail',)
