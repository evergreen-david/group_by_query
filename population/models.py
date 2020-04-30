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

