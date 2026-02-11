from typing import Optional

class Recipient:

    def __init__(self,user_id: str, email: Optional[str],
                 phone: Optional[str], push_tk: Optional[str] ):
        self.user_id = user_id
        self.email = email
        self.phone = phone
        self.push_tk = push_tk
               
    def get_user_id(self) -> str:
        return self.user_id
    
    def get_email(self) -> str:
        return self.email
    
    def get_phone(self) -> str:
        return self.phone
    
    def get_push_token(self) -> str:
        return self.push_tk
