from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .utils import *
# Create your views here.

def index(request):
    return render(request, "teto/index.html")


class ProductClass(DataMixin, ListView):
    model = Product
    template_name = "teto/index.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Product"
        return dict(list(context.items()) + list(c_def.items()))