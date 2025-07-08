from django.db import models

# Create your models here.
class Asignatura(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion
class Laboratorio(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion
class Carrera(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion
    
class Docente(models.Model):
    nombre = models.CharField(max_length=200)
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
    def __str__(self):
         return self.fecha.strftime('%Y-%m-%d') + ' ' + self.hora_inicio.strftime('%H:%M') + ' - ' + self.hora_fin.strftime('%H:%M') + ' | ' + str(self.asignatura_id) + ' | ' + str(self.docentes_id) + ' | ' + str(self.laboratorio_id) + ' | ' + str(self.carreras_id)
