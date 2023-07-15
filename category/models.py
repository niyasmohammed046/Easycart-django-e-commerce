from django.db import models
from django.urls import reverse
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug          = models.SlugField(max_length=150,unique=True)
    description   = models.TextField(max_length=300,blank=True)
    category_image= models.ImageField(upload_to="photos/categories",blank=True)

    class Meta:   #this is to change categorys to categories in the admin panel
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name