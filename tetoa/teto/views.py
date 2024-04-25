from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


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
    
    


class ChangeName(DataMixin, LoginRequiredMixin, FormView):
    form_class = Usermodname
    template_name = 'teto/name.html'
    success_url = reverse_lazy("Home")
    
    def get_form_kwargs(self):
        kwargs = super(ChangeName, self).get_form_kwargs()
        kwargs.update({'instance': self.request.user})
        return kwargs
    
    def form_valid(self, form):
        form.instance.username = form.cleaned_data['username']
        form.instance.save()
        return super(ChangeName, self).form_valid(form)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Смена имени пользователя"
        return dict(list(context.items()) + list(c_def.items()))
    
    
    
    
class tetoCategory(DataMixin, ListView):
    template_name = "teto/index.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Product.objects.all().filter(cat__slug = self.kwargs['cat_slug']).select_related("cat")
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        cat1 = context["posts"][0].cat
        context["title"] = "Категория -" + cat1.name 
        return dict(list(context.items()) + list(c_def.items()))
    
class TagPostList(DataMixin,ListView):
    template_name = 'teto/index.html'
    context_object_name = 'posts'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        tag = TetoTagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Product.objects.all().filter(tags__slug=self.kwargs['tag_slug'])