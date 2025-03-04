from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'username', 'id':'reg-email', 'placeholder':'Enter your Username',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'id':'reg-pass', 'placeholder':'Enter your password',}))

    class Meta:
        model = User
        fields = ['username', 'password']