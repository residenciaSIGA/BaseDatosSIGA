from django.db import models

# Create your models here.

class TipoDoc(models.Model):
    descripcion = models.CharField(max_length = 100)