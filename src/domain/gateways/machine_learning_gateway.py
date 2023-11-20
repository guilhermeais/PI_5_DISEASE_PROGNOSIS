from abc import ABC, abstractmethod
from typing import List

class MachineLearningGateway(ABC):
    @abstractmethod
    def predict(self, symptoms: List[bool]) -> str:
        pass
