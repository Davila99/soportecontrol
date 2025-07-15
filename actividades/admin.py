from django.contrib import admin

from actividades.models import Actividad, TipoActividad

admin.site.register(TipoActividad)
admin.site.register(Actividad)

