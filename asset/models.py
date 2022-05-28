from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey('Employee', on_delete=models.SET_NULL)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
    is_admin = models.BooleanField()

class Asset(models.Model):
    FINE = 'F'
    BROKEN = 'B'
    IN_MAINTENANCE = 'M'
    STATUS_CHOICES = [
        (FINE, 'Fine'),
        (BROKEN, 'Broken'),
        (IN_MAINTENANCE, 'In maintenance'),
    ]

    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=FINE)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)