from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import *
from .utils import *
from .forms import *
# Create your views here.


class ProductClass(DataMixin, ListView):
    model = Product
    template_name = "teto/index.html"
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Главная страница"
        return dict(list(context.items()) + list(c_def.items()))
    
    
class ProdAddClass(DataMixin, CreateView):
    form_class = ProductForm
    template_name = "teto/add_prod.html"
    success_url = reverse_lazy("Home")
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Добавление продукта"
        return dict(list(context.items()) + list(c_def.items()))
    
    

class ShowPost(DataMixin, DetailView):
    model = Product
    template_name = "teto/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = context["posts"].title
        return dict(list(context.items()) + list(c_def.items()))
    
    
class ContactClass(DataMixin,ListView):
    model = Product
    template_name = "teto/contact.html"


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Contact"
        return dict(list(context.items()) + list(c_def.items()))
    
class LoginUserr(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "teto/login.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Авторизация"
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy("Home")
    
    
class RegisterUserr(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "teto/register.html"
    success_url = reverse_lazy("login")
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Регистрация"
        return dict(list(context.items()) + list(c_def.items()))
        
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class UsersClass(DataMixin, ListView):
    model = Product
    template_name = "teto/users.html"
    users = User.objects.all()
    usersname = [user for user in users]
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Пользователи сайта"
        context["usersnames"] = self.usersname
        return dict(list(context.items()) + list(c_def.items()))
    
    
    
    