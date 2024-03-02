from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    slug = models.SlugField(max_length = 255, unique = True, db_index = True )
    photo = models.ImageField(upload_to="photos/", defaut = None)
    price = models.DecimalField( max_digits = 7, decimal_places = 2)
    quantity = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(10000)])
    
                                 