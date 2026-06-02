from rest_framework import serializers
from .model import Pessoa, Departamento, Escala, Evento, EventoDepartamento

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = '__all__'
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class EventoDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoDepartamento
        fields = '__all__'