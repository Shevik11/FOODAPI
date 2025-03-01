from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="images/", default="images/food.jpg")
    def __str__(self):
        return self.name