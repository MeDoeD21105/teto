from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




from .models import *

class ProductForm(forms.ModelForm):
    
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категория")
    
    
    
    class Meta:
        model = Product
        fields = ["title", "slug", "content", "photo", "price", "quantity", "cat"]
        
        #widgets = {
            #представление Django элемента ввода HTML - то как будут ообжаться в html
            #'title': forms.TextInput(attrs={'class': 'form-input'}),
            #'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        #}
        #labes = {"slug": "URL"} изменяет название поля формы
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError("Длина заголовка не должна быть меньше чем 5 символов.")
        return title
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пороль", widget=forms.PasswordInput())
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин")
    password1 = forms.CharField(label="Пароль",  widget=forms.PasswordInput())   
    password2 = forms.CharField(label=" Повтор пароля", widget=forms.PasswordInput())
    
    #class Meta:
     #   model = get_user_model()
        #fields = ["username", "password", "password2" ]
        
     
                 
class Usermodname(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]

        