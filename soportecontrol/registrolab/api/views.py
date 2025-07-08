from rest_framework import viewsets
from registrolab.models import RegistroLab
from registrolab.api.serializers import RegistroLabSerializer


class RegistroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RegistroLab to be viewed or edited.
    """
    queryset = RegistroLab.objects.all()
    serializer_class = RegistroLabSerializer
