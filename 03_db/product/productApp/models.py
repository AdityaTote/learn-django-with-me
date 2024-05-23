from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='productsImg/')
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    rate = models.IntegerField(range(1,5))
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name