from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, related_name='food_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
