from django.db import models


class Restaurant(models.Model):
    """
    To register a restaurant, the model will require some information, such as:

    Restaurant name, Address, Phone number, Owner's name
    """
    email = models.EmailField()
    password = models.CharField(max_length=256)
    token_id = models.CharField(max_length=256, default='No token id provided.')

    restaurant_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.restaurant_name


class Dishes(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    dish_name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=500)

    def __str__(self):
        return self.dish_name


class Client(models.Model):
    """
    To register a client, the model will require some information, such as:

    Email, password, token_id, client name, client's address
    """
    email = models.EmailField()
    password = models.CharField(max_length=256)
    token_id = models.CharField(max_length=256, default='No token id provided.')

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.name
