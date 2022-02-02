from django import forms
from .models import User
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput

class SendBackForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SendBackForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['name', 'email', 'message']

    # widgets = {
    #     'name': TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'ФИО'
    #     }),
    #     'email': TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Ваша почта'
    #     }),
    #     'text': TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Ваше сообщение'
    #     })
    # }