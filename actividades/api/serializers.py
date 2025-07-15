from rest_framework import serializers
from actividades.models import TipoActividad, Actividad
from registrolab.api.serializers import DocenteSerializer
from registrolab.models import Docente


class TipoActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActividad
        fields = '__all__'  # O especifica campos: ['id', 'descripcion']


class ActividadSerializer(serializers.ModelSerializer):
    # Serializers anidados para relaciones
    tipo = TipoActividadSerializer(read_only=True)
    tipo_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoActividad.objects.all(),
        source='tipo',
        write_only=True
    )
    docente_responsable = DocenteSerializer(read_only=True)
    docente_responsable_id = serializers.PrimaryKeyRelatedField(
        queryset=Docente.objects.all(),
        source='docente_responsable',
        write_only=True,
        allow_null=True
    )

    # Campo personalizado para mostrar el estado legible
    estado_display = serializers.CharField(
        source='get_estado_display',
        read_only=True
    )

    class Meta:
        model = Actividad
        fields = [
            'id',
            'titulo',
            'tipo', 'tipo_id',
            'descripcion',
            'fecha',
            'estado', 'estado_display',
            'enlaces',
            'requisitos',
            'docente_responsable', 'docente_responsable_id',
            'fecha_creacion',
            'fecha_modificacion'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_modificacion']