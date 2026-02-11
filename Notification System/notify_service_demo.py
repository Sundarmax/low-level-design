
from notification.notification_service import NotificationService
from entities.recipient import Recipient
from entities.notification import Notification
from enums.notification_type import NotificationType

notify_service = NotificationService(5)

recipient1 = Recipient("sundarmax12", "max@gmail.com", None, "token123")
recipient2 = Recipient("sundarmax11", "max1@gmail.com", "95004904", "token1234")

test_sms = (Notification.Builder(recipient2,NotificationType.SMS) \
    .subject("TEst SMS").message("TEST MEssage").build())


notify_service.send_notification(test_sms)
