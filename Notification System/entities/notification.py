from .recipient import Recipient
from enums.notification_type import NotificationType
import uuid

class Notification:

    def __init__(self, builder):
        self.id = str(uuid.uuid4())
        self.recipient = builder.recipient
        self.notify_type = builder.notify_type
        self._message = builder._message
        self._subject = builder._subject
    
    def get_id(self) -> str:
        return self.id
    
    def get_recipient(self) -> str:
        return self.recipient
    
    def get_type(self) -> NotificationType:
        return self.notify_type
    
    def get_message(self) -> str:
        return self._message
    
    def get_sbject(self) -> str:
        return self._subject
        
    class Builder:
        
        def __init__(self, recipient : Recipient, notify_type : NotificationType):
            self.recipient = recipient
            self.notify_type = notify_type
            self._message = None
            self._subject = None

        def message(self, message : str):
            self._message = message
            return self

        def subject(self, subject: str):
            self._subject = subject
            return self
        
        def build(self):
            return Notification(self)
        
