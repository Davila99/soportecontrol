from rest_framework import viewsets
from registrolab.models import RegistroLab, Asignatura, Docente, Laboratorio, Carrera

from .serializers import (
    RegistroLabSerializer,
    AsignaturaSerializer,
    DocenteSerializer,
    LaboratorioSerializer,
    CarreraSerializer
)


class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer


class RegistroLabViewSet(viewsets.ModelViewSet):
    queryset = RegistroLab.objects.select_related(
        "asignatura_id",
        "docentes_id",
        "laboratorio_id",
        "carreras_id"
    )
    serializer_class = RegistroLabSerializer
