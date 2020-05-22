from django.db import models
from datetime import date
from django.contrib.auth import get_user_model

# Create your models here.
class bajada(models.Model):
    ancho = models.IntegerField(null=True)
    diametro = models.IntegerField(null=True)
    gramaje = models.IntegerField(null=True)
    peso = models.IntegerField(null=True)
    bobinanro = models.IntegerField(null=True)
    ofnro = models.IntegerField(null=True)
    fecha = models.DateField(auto_now_add=True)    
    turno = models.CharField(max_length=1)
    calidad = models.IntegerField(null=True)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    usuariocreacion = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    fechaultmod = models.DateTimeField(auto_now_add=True)
    usuarioultmod = None 

class Meta:
    ordering = ["-id"]

def __str__(self):
        return self.id