# actividades/views.py
from rest_framework import viewsets

from actividades.models import Actividad, TipoActividad

from .serializers import TipoActividadSerializer, ActividadSerializer

class TipoActividadViewSet(viewsets.ModelViewSet):
    queryset = TipoActividad.objects.all()
    serializer_class = TipoActividadSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer