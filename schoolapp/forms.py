from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import field


class RegisterForm(forms.ModelForm):
    class Meta:
        model = field
        fields = "__all__"


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=True, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'name': 'username' }))
    password = forms.CharField(label="Password", required=True, max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'name': 'password' }))
