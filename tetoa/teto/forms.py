from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "slug", "content", "photo", "price", "quantity"]
        
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пороль")
    
class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль",  widget=forms.PasswordInput())   
    password2 = forms.CharField(label=" Повтор пароля", widget=forms.PasswordInput())
    
    class Meta:
        model = get_user_model()
        fields = ["username", "password", "password2" ]