from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Asignatura(models.Model):
    descripcion = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.descripcion


class Laboratorio(models.Model):
    descripcion = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.descripcion


class Carrera(models.Model):
    descripcion = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.descripcion


class Docente(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre


class RegistroLab(models.Model):
    fecha = models.DateField('Fecha')
    asignatura_id = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    docentes_id = models.ForeignKey(Docente, on_delete=models.CASCADE)
    laboratorio_id = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    carreras_id = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    hora_inicio = models.TimeField('Hora Entrada')
    hora_fin = models.TimeField('Hora Salida')

    def clean(self):

        if self.hora_inicio >= self.hora_fin:
            raise ValidationError(
                "La hora de inicio debe ser menor que la hora de salida."
            )

        conflicto_lab = RegistroLab.objects.filter(
            laboratorio_id=self.laboratorio_id,
            fecha=self.fecha,
            hora_inicio__lt=self.hora_fin,
            hora_fin__gt=self.hora_inicio
        ).exclude(id=self.id)

        if conflicto_lab.exists():
            raise ValidationError(
                "Este laboratorio ya está reservado en ese horario."
            )

        conflicto_docente = RegistroLab.objects.filter(
            docentes_id=self.docentes_id,
            fecha=self.fecha,
            hora_inicio__lt=self.hora_fin,
            hora_fin__gt=self.hora_inicio
        ).exclude(id=self.id)

        if conflicto_docente.exists():
            raise ValidationError(
                "Este docente ya tiene una reserva en ese horario"
            )

    def __str__(self):
        return (
            f"{self.fecha.strftime('%Y-%m-%d')} "
            f"{self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')} | "
            f"{self.asignatura_id} | {self.docentes_id} | {self.laboratorio_id} | {self.carreras_id}"
        )
