from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.DateField()
    doors = models.IntegerField()

    def __str__(self):
        return self.model

