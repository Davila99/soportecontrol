from django.contrib import admin
from .models import RegistroLab, Laboratorio, Asignatura, Carrera, Docente


# ---------------------------------
# LABORATORIO
# ---------------------------------
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)
    ordering = ("descripcion",)


# ---------------------------------
# ASIGNATURA
# ---------------------------------
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)
    ordering = ("descripcion",)


# ---------------------------------
# CARRERA
# ---------------------------------
@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)
    ordering = ("descripcion",)


# ---------------------------------
# DOCENTE
# ---------------------------------
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    ordering = ("nombre",)


# ---------------------------------
# REGISTRO LAB (PRINCIPAL)
# ---------------------------------
@admin.register(RegistroLab)
class RegistroLabAdmin(admin.ModelAdmin):

    # 🔹 Columnas visibles
    list_display = (
        "fecha",
        "asignatura_id",
        "docentes_id",
        "laboratorio_id",
        "carreras_id",
        "hora_inicio",
        "hora_fin",
    )

    # 🔎 BUSCADOR PRINCIPAL (arriba)
    search_fields = (
        "asignatura_id__descripcion",
        "docentes_id__nombre",
        "laboratorio_id__descripcion",
        "carreras_id__descripcion",
        "fecha",
    )

    # 🔽 Filtros laterales
    list_filter = (
        "asignatura_id",
        "docentes_id",
        "laboratorio_id",
        "carreras_id",
        "fecha",
    )

    date_hierarchy = "fecha"

    ordering = ("-fecha", "hora_inicio")
    list_per_page = 25

    # 🚀 OPTIMIZACIÓN (como tu módulo Libro)
    autocomplete_fields = (
        "asignatura_id",
        "docentes_id",
        "laboratorio_id",
        "carreras_id",
    )

    list_select_related = (
        "asignatura_id",
        "docentes_id",
        "laboratorio_id",
        "carreras_id",
    )
