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
    laboratorio = LaboratorioSerializer(
        source='laboratorio_id', read_only=True)
    carrera = CarreraSerializer(source='carreras_id', read_only=True)

    class Meta:
        model = RegistroLab
        fields = '__all__'

    def validate(self, data):

        docentes_id = data.get('docentes_id')
        laboratorio = data.get('laboratorio_id')
        fecha = data.get('fecha')
        hora_inicio = data.get('hora_inicio')
        hora_fin = data.get('hora_fin')

        # validar rango de horas
        if hora_inicio >= hora_fin:
            raise serializers.ValidationError(
                "La hora de inicio debe ser menor que la hora de salida."
            )

        # -------- VALIDAR DOCENTE --------
        conflicto_docente = RegistroLab.objects.filter(
            docentes_id=docentes_id,
            fecha=fecha,
            hora_inicio__lt=hora_fin,
            hora_fin__gt=hora_inicio
        )

        if self.instance:
            conflicto_docente = conflicto_docente.exclude(id=self.instance.id)

        if conflicto_docente.exists():
            raise serializers.ValidationError(
                "Este docente ya tiene una reserva en ese horario."
            )

        # -------- VALIDAR LABORATORIO --------
        conflicto_lab = RegistroLab.objects.filter(
            laboratorio_id=laboratorio,
            fecha=fecha,
            hora_inicio__lt=hora_fin,
            hora_fin__gt=hora_inicio
        )

        if self.instance:
            conflicto_lab = conflicto_lab.exclude(id=self.instance.id)

        if conflicto_lab.exists():
            raise serializers.ValidationError(
                "Este laboratorio ya está reservado en ese horario."
            )

        return data
