from sqlite3 import Cursor
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Pelicula(models.Model):
    nom_pelicula = models.CharField(max_length=50)
    resumen = models.TextField(max_length=300)
    genero = models.CharField(max_length=20)
    duracion = models.PositiveIntegerField()
    reparto = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nom_pelicula

    def get_absolute_url(self):
        return reverse("pelicula_detalle", args=[str(self.id)])
