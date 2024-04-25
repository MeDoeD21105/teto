from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(TetoTagPost)