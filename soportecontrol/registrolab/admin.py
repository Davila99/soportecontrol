from django.contrib import admin
from actividades.models import Actividad, TipoActividad
from registrolab.models import RegistroLab,Laboratorio,Asignatura,Carrera,Docente
# Register your models here.
admin.site.register(RegistroLab)
admin.site.register(Laboratorio)
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Docente)
