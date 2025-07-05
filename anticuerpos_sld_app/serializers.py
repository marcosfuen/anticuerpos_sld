from rest_framework import serializers
from .models import Resultado, TipoTest, Paciente

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ['nombre']

class TipoTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTest
        fields = ['nombre']

class PacienteSerializer(serializers.ModelSerializer):
    tipoTest = TipoTestSerializer()
    resultado = ResultadoSerializer()
    class Meta:
        model = Paciente
        fields = ['carIdentidad', 'nombresApellidos', 'tipoTest', 'resultado', 'fecha', 'fechaRecibido']