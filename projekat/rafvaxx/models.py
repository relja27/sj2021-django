from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    doses = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(3)], default='')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    year = models.IntegerField()
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name