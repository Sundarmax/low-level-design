from entities.notification import Notification
from factory.notification_factory import NotificationFactory

from concurrent.futures import ThreadPoolExecutor

# facade pattern
class NotificationService:

    def __init__(self, pool_size : int):
        self.executor = ThreadPoolExecutor(max_workers=pool_size)

    def send_notification(self, notification : Notification):
        
        def send_task():
            gateway = NotificationFactory.create_gateway(notification.get_type())
            try:
                gateway.send(notification)
            except Exception as e:
                print(f"Exception while sending notification: {e}")
            
        self.executor.submit(send_task)
        
    def shutdown(self):
        self.executor.shutdown()