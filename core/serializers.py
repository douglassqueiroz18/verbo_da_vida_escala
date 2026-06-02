from rest_framework import serializers
from .models import Pessoa, Departamento, Escala, Evento

class PessoaSerializer(serializers.ModelSerializer):
    departamentos = serializers.PrimaryKeyRelatedField(many=True, queryset=Departamento.objects.all())

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

    def validate(self, attrs):
        data = attrs.get('data', getattr(self.instance, 'data', None))
        pessoa = attrs.get('pessoa', getattr(self.instance, 'pessoa', None))

        if data and pessoa:
            conflict = Escala.objects.filter(
                pessoa=pessoa,
                data__date=data.date(),
                data__hour=data.hour,
                data__minute=data.minute,
            )
            if self.instance:
                conflict = conflict.exclude(pk=self.instance.pk)

            if conflict.exists():
                raise serializers.ValidationError({
                    'non_field_errors': [
                        'Esta pessoa já está escalada no mesmo dia e horário.'
                    ]
                })

        return attrs

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
