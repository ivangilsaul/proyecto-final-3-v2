from django.db import models

class Avion(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - {self.color}"