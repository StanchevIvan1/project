from django import forms
from django.contrib.auth.forms import UsernameField

from watch_shop.auth_app.models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'photo')
        field_classes = {'username': UsernameField}
