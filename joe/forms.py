from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . models import Product, User, EmailMsg
from django.template.defaultfilters import filesizeformat
from django.conf import settings
from jinjo.settings import CONTENT_TYPES, MAX_UPLOAD_SIZE
from django.core.validators import FileExtensionValidator
from .formval import clean_file


class EmailForm(forms.ModelForm):
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True )
    message = forms.CharField(required=True, label='message', widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'email',
                                                                     'placeholder': 'message', 'spellcheck': 'true',
                                                                  'rows': 5, 'cols': 50}))
    
    class Meta:
        model = EmailMsg
        fields = ['name', 'email', 'message']                                                              



