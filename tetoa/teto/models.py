from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator




def vaalidator_erors(name):
    if len(name) < 3:
        raise ValidationError("Слишком короткое имя для продукта")
    else:
        return name
    

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255,verbose_name="Название",)
    slug = models.SlugField(unique = True, db_index = True, verbose_name="URL", validators=[MinLengthValidator(4, message="минимальное количество символов в Url, дожно быть 4")])
    content = models.TextField(blank = True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/", default=None, blank=True, null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    price = models.DecimalField( max_digits = 7, decimal_places = 2, verbose_name="Цена")
    quantity = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(10000)], verbose_name="Количество")
    cat = models.ForeignKey("Category", on_delete = models.PROTECT, verbose_name="Категория товара",)
    tags = models.ManyToManyField('TetoTagPost', blank=True, related_name='tags', verbose_name="Теги")
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug":self.slug})


    def __str__(self):
        return self.title
    
    
    
class Category(models.Model):
    name = models.CharField(max_length = 255, db_index = True,)
    slug = models.CharField(max_length = 255, db_index = True, unique = True)
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug" : self.slug })
    
    def __str__(self):
        return self.name

class TetoTagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})