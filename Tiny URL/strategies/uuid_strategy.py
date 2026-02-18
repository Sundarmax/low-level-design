
from .key_gen_strategy import KeyGenerationStrategy
import uuid

class UUIDStrategy(KeyGenerationStrategy):
    KEY_LENGTH = 6
    def generate_key(self, id: int) -> str:
        uuid_str = str(uuid.uuid4()).replace("-","")
        return uuid_str[: self.KEY_LENGTH]