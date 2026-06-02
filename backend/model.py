from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=50)
    disponibilidade = models.CharField(max_length=255, blank=True, null=True)
    limite_mensal = models.IntegerField()

class Departamento(models.Model):
    nome = models.CharField(max_length=255)

class Escala(models.Model):
    data = models.DateField()
    status_alocacao = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    tipo_evento = models.CharField(max_length=100)

class EventoDepartamento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)