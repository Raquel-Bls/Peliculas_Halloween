from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=30)
    Edad = models.PositiveIntegerField(null=True, blank=True)
