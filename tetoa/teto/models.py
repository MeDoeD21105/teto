from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, db_index = True)
    content = models.TextField(blank = True)
    photo = models.ImageField(upload_to="photos/", default=None, blank=True, null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    price = models.DecimalField( max_digits = 7, decimal_places = 2)
    quantity = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(10000)])
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug":self.slug})
        
    
    def __str__(self):
        return self.title
    