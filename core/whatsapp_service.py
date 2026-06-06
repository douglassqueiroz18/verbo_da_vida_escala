import pywhatkit as kit
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class WhatsAppService:
    """Serviço para enviar mensagens via WhatsApp usando pywhatskit"""
    
    @staticmethod
    def enviar_mensagem(numero: str, mensagem: str, agora: bool = False):
        """
        Envia mensagem de WhatsApp gratuitamente
        
        Args:
            numero: Número com código do país (ex: "+55 11 98765-4321")
            mensagem: Texto da mensagem
            agora: Se True, envia imediatamente. Se False, agenda para 2 minutos
        """
        try:
            # Remove caracteres especiais do número
            numero_limpo = numero.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
            
            if agora:
                # Envia imediatamente (browser abre automaticamente)
                kit.sendwhatmsg_instantly(numero_limpo, mensagem, wait_time=15)
            else:
                # Agenda para 2 minutos no futuro
                agora_datetime = datetime.now() + timedelta(minutes=2)
                kit.sendwhatmsg(
                    phone_no=numero_limpo,
                    message=mensagem,
                    time_hour=agora_datetime.hour,
                    time_min=agora_datetime.minute,
                    wait_time=15
                )
            
            logger.info(f"Mensagem enviada para {numero_limpo}")
            return {"sucesso": True, "mensagem": "Mensagem enviada com sucesso"}
        
        except Exception as e:
            logger.error(f"Erro ao enviar mensagem: {str(e)}")
            return {"sucesso": False, "erro": str(e)}
    
    @staticmethod
    def enviar_para_grupo(id_grupo: str, mensagem: str):
        """Envia mensagem para um grupo do WhatsApp"""
        try:
            kit.sendwhatmsg_to_group(id_grupo, mensagem, wait_time=15)
            logger.info(f"Mensagem enviada para grupo {id_grupo}")
            return {"sucesso": True, "mensagem": "Mensagem enviada para o grupo"}
        except Exception as e:
            logger.error(f"Erro ao enviar para grupo: {str(e)}")
            return {"sucesso": False, "erro": str(e)}