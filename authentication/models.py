from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ["email", "type"]
    TYPE_MANAGER = 'M'
    TYPE_COMANAGER = 'C'
    TYPE_EMPLOYEE = 'E'

    TYPES_CHOICES = [
        (TYPE_MANAGER, 'Manager'),
        (TYPE_COMANAGER, 'Co-Manager'),
        (TYPE_EMPLOYEE, 'Employee'),
    ]
    type = models.CharField(max_length=1, choices=TYPES_CHOICES, default=TYPE_EMPLOYEE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile/images')

