from django import forms
from django.core.mail.message import EmailMessage

from core.models import FeedbackModel

class FeedbackForms(forms.ModelForm):
    class Meta:
        '''
        Passando os metadados.
        '''
        model = FeedbackModel
        fields = ['nome', 'OM', 'email', 'message']
