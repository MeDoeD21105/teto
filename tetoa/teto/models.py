from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255, verbose_name="Название")
    slug = models.SlugField(unique = True, db_index = True, verbose_name="URL")
    content = models.TextField(blank = True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/", default=None, blank=True, null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    price = models.DecimalField( max_digits = 7, decimal_places = 2, verbose_name="Цена")
    quantity = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(10000)], verbose_name="Количество")
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug":self.slug})


    def __str__(self):
        return self.title
