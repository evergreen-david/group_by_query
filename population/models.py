from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'countries'


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    population = models.PositiveIntegerField()

    class Meta:
        db_table = 'cities'

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'products'

class Order(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'orders'


