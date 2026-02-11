
from enums.notification_type import NotificationType
from strategies.notification_gateway import NotificationGateway
from strategies.sms_gateway import SmsGateway

class NotificationFactory:

    # Use caching (gatewayMap) to reuse gateway instances

    @classmethod
    def create_gateway(cls, notification_type: NotificationType) -> NotificationGateway:
        gateway = None
        if notification_type == NotificationType.EMAIL:
            pass
        if notification_type == NotificationType.SMS:
            gateway = SmsGateway()
        return gateway
