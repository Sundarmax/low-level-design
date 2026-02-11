from .notification_gateway import NotificationGateway
from entities.notification import Notification

class SmsGateway(NotificationGateway):

    def send(self, notification : Notification):
        phone = notification.get_recipient().get_phone()
        if not phone:
            raise ValueError("Phone no is required")
        print("--- Sending SMS ---")
        print(f"To: {phone}")
        print(f"Message: {notification.get_message()}")
        print("-------------------\n")