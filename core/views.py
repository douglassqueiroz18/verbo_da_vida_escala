from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Pessoa, Departamento, Escala, Evento
from .serializers import PessoaSerializer, DepartamentoSerializer, EscalaSerializer, EventoSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['departamentos']
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer
    def perform_create(self, serializer):
        print("Escala recebida:", self.request.data.get("data"))
        return serializer.save()
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

