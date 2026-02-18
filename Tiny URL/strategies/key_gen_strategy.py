from abc import ABC,abstractmethod

class KeyGenerationStrategy(ABC):
    
    @abstractmethod
    def generate_key(self, id: int) -> str:
        pass