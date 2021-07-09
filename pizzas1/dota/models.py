from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    class Meta:
        app_label = 'dota'
        db_table = 'dota.restaurants'
    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField('name', max_length=128, blank=True)
    cheese = models.CharField('cheese', max_length=128, blank=True)
    pastry = models.CharField('pastry', max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    class Meta:
        app_label = 'dota'
        db_table = 'dota.pizzas1'
    def __str__(self):
        return self.name

