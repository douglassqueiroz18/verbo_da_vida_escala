from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=255)

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=50)
    # Mesclando campos dos dois arquivos
    disponibilidade = models.CharField(max_length=255, blank=True, null=True)
    limite_mensal = models.IntegerField(default=0)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    departamentos = models.ManyToManyField(Departamento, blank=True, related_name='pessoas')

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()
    tipo_evento = models.CharField(max_length=100)

class Escala(models.Model):
    data = models.DateTimeField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True, null=True)
    notificacao_24h_enviada = models.BooleanField(default=False)
    notificacao_2h_enviada = models.BooleanField(default=False)
    status_alocacao = models.CharField(max_length=100, blank=True, null=True)

class EventoDepartamento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)