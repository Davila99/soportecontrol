from rest_framework import serializers
from registrolab.models import RegistroLab, Asignatura, Docente, Laboratorio, Carrera




# -------- MODELOS RELACIONADOS --------

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


# -------- REGISTRO LAB --------

class RegistroLabSerializer(serializers.ModelSerializer):

    # Para mostrar datos completos (lectura)
    asignatura = AsignaturaSerializer(source='asignatura_id', read_only=True)
    docente = DocenteSerializer(source='docentes_id', read_only=True)
    laboratorio = LaboratorioSerializer(source='laboratorio_id', read_only=True)
    carrera = CarreraSerializer(source='carreras_id', read_only=True)

    class Meta:
        model = RegistroLab
        fields = '__all__'
