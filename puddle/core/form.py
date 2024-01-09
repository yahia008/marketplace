from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class Login(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'username',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'password',
            'class':'w-full py-4 px-6 rounded-xl'
        }))



class SignUp(UserCreationForm):

    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'username',
            'class':'w-full py-4 px-6 rounded-xl'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder':'Email',
            'class':'w-full py-4 px-6 rounded-xl'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'password',
            'class':'w-full py-4 px-6 rounded-xl'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'confirm password',
            'class':'w-full py-4 px-6 rounded-xl'
        }))