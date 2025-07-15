from django.db import models

from registrolab.models import Docente
class TipoActividad(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class Actividad(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_CURSO', 'En curso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)
    descripcion = models.TextField()
    objetivo = models.TextField()
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    enlaces = models.JSONField(default=list)
    requisitos = models.TextField(blank=True)
    docente_responsable = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"