from firebase_admin import messaging

class NotificationService:
    @staticmethod
    def send_push(token, title, body, data=None):
        try:
            message = messaging.Message(
                token=token,
                notification=messaging.Notification(title=title, body=body),
                data=data or {}
            )
            response = messaging.send(message)
            return {"sucesso": True, "response": response}
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}