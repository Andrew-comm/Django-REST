from django.db import models

# Create your models here.
class Drink(models.Model):
    name =  models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField
    alcoholic = models.BooleanField(default=False)

    def __str__(self) :
        return self.name