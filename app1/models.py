from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    opening = models.BooleanField(default=False)

    def __str__(self):
        return self.name
