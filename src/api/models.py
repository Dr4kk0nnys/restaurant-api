from django.db import models


class RestaurantRegister(models.Model):
    """
    To register a restaurant the model will require some information, such as:

    Restaurant name, Address, Phone number, Owner's name
    """
    restaurant_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.restaurant_name
