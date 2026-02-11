from abc import ABC,abstractmethod
from entities.notification import Notification

class NotificationGateway(ABC):
    @abstractmethod
    def send(self, notification : Notification ):
        pass
