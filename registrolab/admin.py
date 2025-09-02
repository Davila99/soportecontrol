from django.contrib import admin
from .models import RegistroLab, Laboratorio, Asignatura, Carrera, Docente

# ------------------------------
# Admin para RegistroLab
# ------------------------------
@admin.register(RegistroLab)
class RegistroLabAdmin(admin.ModelAdmin):
    list_display = ("fecha", "asignatura_id", "docentes_id", "laboratorio_id", "carreras_id", "hora_inicio", "hora_fin")
    search_fields = (
        "asignatura_id__descripcion",
        "docentes_id__nombre",
        "laboratorio_id__descripcion",
        "carreras_id__descripcion",
    )
    list_filter = ("asignatura_id", "docentes_id", "laboratorio_id", "carreras_id", "fecha")
    date_hierarchy = "fecha"

# ------------------------------
# Admin para Laboratorio
# ------------------------------
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)

# ------------------------------
# Admin para Asignatura
# ------------------------------
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)

# ------------------------------
# Admin para Carrera
# ------------------------------
@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)

# ------------------------------
# Admin para Docente
# ------------------------------
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
