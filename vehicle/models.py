from django.db import models


# Create your models here.
class Types(models.Model):
    vehicle_type = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicle_type


class Vehicles(models.Model):
    vehicle_number = models.CharField(max_length=10)
    vehicle_type = models.ForeignKey(Types, related_name='vehicle', on_delete=models.CASCADE)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
