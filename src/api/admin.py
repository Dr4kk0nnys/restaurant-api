from django.contrib import admin

from api.models import Restaurant, Dishes, Client


"""
Although the user admin should be able to controll the dishes and restaurants,
The only way of the user to controll ( add, remove, update ) dishes is through proper
api calling.
"""

class DishesInline(admin.StackedInline):
    model = Dishes
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    fields = ['email', 'password', 'restaurant_name', 'owner_name', 'address', 'phone_number', 'token_id']
    inlines = [DishesInline]


class ClientAdmin(admin.ModelAdmin):
    fields = ['email', 'password', 'name', 'address', 'token_id']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Client, ClientAdmin)
