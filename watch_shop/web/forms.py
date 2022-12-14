from django import forms
from django.contrib.auth.forms import UsernameField

from watch_shop.auth_app.models import Profile
from watch_shop.web.models import Product


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'photo')
        field_classes = {'username': UsernameField}


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
