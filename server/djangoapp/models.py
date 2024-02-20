'''ORM Django models'''
from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    '''Model for car make'''
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class CarModel(models.Model):
    '''Model for car model'''
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('CROSSOVER', 'Crossover'),
        ('COMPACT', 'Compact'),
        ('TRUCK', 'Truck')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2024,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return str(self.name)
