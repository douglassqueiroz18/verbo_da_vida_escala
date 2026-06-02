from rest_framework import status
from rest_framework.test import APITestCase

from .models import Pessoa, Departamento, Evento, Escala, EventoDepartamento

class PessoaAPITestCase(APITestCase):
    def setUp(self):
        self.p1 = Pessoa.objects.create(
            nome='João Silva',
            telefone='11999999999',
            disponibilidade='Segunda a Sexta',
            limite_mensal=40
        )
        self.p2 = Pessoa.objects.create(
            nome='Maria Souza',
            telefone='21988888888',
            disponibilidade='Terça e Quinta',
            limite_mensal=30
        )
        self.url = '/api/pessoas/'

    def test_list_pessoas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_pessoa(self):
        data = {
            "nome": "Carlos Lima",
            "telefone": "11977777777",
            "disponibilidade": "Segunda",
            "limite_mensal": 20
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pessoa.objects.count(), 3)

    def test_retrieve_pessoa(self):
        response = self.client.get(f'{self.url}{self.p1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'João Silva')


class DepartamentoAPITestCase(APITestCase):
    def setUp(self):
        self.d1 = Departamento.objects.create(nome='Recursos Humanos')
        self.url = '/api/departamentos/'

    def test_list_departamentos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_departamento(self):
        response = self.client.post(self.url, {'nome': 'Financeiro'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Departamento.objects.count(), 2)

    def test_retrieve_departamento(self):
        response = self.client.get(f'{self.url}{self.d1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Recursos Humanos')


class EventoAPITestCase(APITestCase):
    def setUp(self):
        self.e1 = Evento.objects.create(
            nome='Reunião',
            data='2026-06-10',
            tipo_evento='Interno'
        )
        self.url = '/api/eventos/'

    def test_list_eventos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_evento(self):
        data = {
            "nome": "Treinamento",
            "data": "2026-06-15",
            "tipo_evento": "Externo"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Evento.objects.count(), 2)

    def test_retrieve_evento(self):
        response = self.client.get(f'{self.url}{self.e1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Reunião')


class EscalaAPITestCase(APITestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome='João Silva',
            telefone='11999999999',
            disponibilidade='Segunda a Sexta',
            limite_mensal=40
        )
        self.departamento = Departamento.objects.create(nome='TI')
        self.url = '/api/escalas/'

    def test_create_escala(self):
        data = {
            "data": "2026-06-20",
            "status_alocacao": "Confirmado",
            "pessoa": self.pessoa.id,
            "departamento": self.departamento.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Escala.objects.count(), 1)

    def test_list_escalas(self):
        Escala.objects.create(
            data='2026-06-20',
            status_alocacao='Confirmado',
            pessoa=self.pessoa,
            departamento=self.departamento
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class EventoDepartamentoAPITestCase(APITestCase):
    def setUp(self):
        self.evento = Evento.objects.create(
            nome='Cerimônia',
            data='2026-06-25',
            tipo_evento='Especial'
        )
        self.departamento = Departamento.objects.create(nome='Marketing')
        self.url = '/api/evento_departamentos/'

    def test_create_evento_departamento(self):
        data = {
            "evento": self.evento.id,
            "departamento": self.departamento.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventoDepartamento.objects.count(), 1)

    def test_list_evento_departamentos(self):
        EventoDepartamento.objects.create(
            evento=self.evento,
            departamento=self.departamento
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)