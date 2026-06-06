from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from core.models import Escala
from core.notificacoes import NotificationService
class Command(BaseCommand):
    help = 'Verifica escalas nas próximas 24h e 2h e envia notificação'

    def handle(self, *args, **options):
        agora = timezone.now()
        em_2h = agora + timedelta(hours=2)
        em_24h = agora + timedelta(hours=24)

        escalas = Escala.objects.filter(data__gte=agora, data__lte=em_24h)

        for escala in escalas:
            token = escala.pessoa.fcm_token
            if not token:
                continue

            if agora <= escala.data <= em_2h and not escala.notificacao_2h_enviada:
                title = "Escala em até 2 horas"
                body = f"Oi {escala.pessoa.nome}, você estará servindo em {escala.departamento.nome} às {escala.data.strftime('%d/%m %H:%M')}."
                tipo = '2h'
            elif em_2h < escala.data <= em_24h and not escala.notificacao_24h_enviada:
                title = "Escala em 24 horas"
                body = f"Oi {escala.pessoa.nome}, você está escalado para {escala.departamento.nome} em {escala.data.strftime('%d/%m %H:%M')}."
                tipo = '24h'
            else:
                continue

            resultado = NotificationService.send_push(token, title, body, {"escala_id": str(escala.id)})

            if resultado['sucesso']:
                if tipo == '2h':
                    escala.notificacao_2h_enviada = True
                else:
                    escala.notificacao_24h_enviada = True
                escala.save()