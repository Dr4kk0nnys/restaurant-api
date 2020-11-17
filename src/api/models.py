from django.db import models


class Restaurant(models.Model):
    """
    To register a restaurant the model will require some information, such as:

    Restaurant name, Address, Phone number, Owner's name
    """
    restaurant_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    token_id = models.CharField(max_length=256)

    objects = models.Manager()

    def __str__(self):
        return self.restaurant_name


class Dishes(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    dish_name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)

    def __str__(self):
        return self.dish_name
