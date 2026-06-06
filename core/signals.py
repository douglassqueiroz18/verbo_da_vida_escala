from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin import messaging
from rest_framework import response

from core.notificacoes import NotificationService
from .models import Escala

@receiver(post_save, sender=Escala)
def enviar_notificacao(sender, instance, created, **kwargs):
    if created:
        token = instance.pessoa.fcm_token
        if token:
            NotificationService.send_push(
                token,
                f"Escala em {instance.departamento.nome}",
                f"Oi {instance.pessoa.nome}, você está escalado para {instance.departamento.nome} em {instance.data.strftime('%d/%m %H:%M')}."
            )
    print('Mensagem enviada com sucesso:', response)