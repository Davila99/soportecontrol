from rest_framework import serializers
from registrolab.models import RegistroLab, Asignatura, Docente, Laboratorio, Carrera

# 1. Primero define serializadores para los modelos relacionados
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

# 2. Luego modifica tu RegistroLabSerializer
class RegistroLabSerializer(serializers.ModelSerializer):
    # Usa los serializadores para los campos relacionados
    asignatura_id = AsignaturaSerializer()
    docentes_id = DocenteSerializer()
    laboratorio_id = LaboratorioSerializer()
    carreras_id = CarreraSerializer()
    
    class Meta:
        model = RegistroLab
        fields = '__all__'