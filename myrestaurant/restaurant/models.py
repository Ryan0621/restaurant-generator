from django.db import models
from address.models import AddressField

# Create your models here.
class OpeningTime(models.Model):
    WEEKDAYS = (
       (1, 'Monday'),
       (2, 'Tuesday'),
       (3, 'Wednesday'),
       (4, 'Thursday'),
       (5, 'Friday'),
       (6, 'Saturday'),
       (7, 'Sunday'),
    )
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    def __str__(self):
        return self.WEEKDAYS[self.weekday - 1][1] + " " + str(self.from_hour) + "-" + str(self.to_hour)

class OutletType(models.Model):
    outlet_type = models.CharField(max_length=20)
    def __str__(self):
        return self.outlet_type


class CuisineType(models.Model):
    cuisine_type = models.CharField(max_length=20)
    def __str__(self):
        return self.cuisine_type

class Affordability(models.Model):
    class Meta:
        verbose_name_plural = "Affordabilities"

    affordability = models.CharField(max_length=20)
    def __str__(self):
        return self.affordability

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = AddressField(on_delete=models.CASCADE)
    outlet_type = models.ForeignKey(OutletType, on_delete=models.CASCADE)
    cuisine_type = models.ForeignKey(CuisineType, on_delete=models.CASCADE)
    affordability = models.ForeignKey(Affordability, on_delete=models.CASCADE)
    opening_times = models.ManyToManyField(OpeningTime)
    vegan_friendly= models.BooleanField()
    halal=models.BooleanField()
    def __str__(self):
        return self.name
