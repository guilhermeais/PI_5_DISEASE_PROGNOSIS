from typing import Dict
from src.domain.gateways.machine_learning_gateway import MachineLearningGateway
from src.domain.entities.symptoms import ALL_POSSIBLE_SYMPTOMS
from src.domain.entities.prognoses_translations import PROGNOSES_TRANSLATIONS

class PrognosisUseCase:
    def __init__(self, machine_learning_gateway: MachineLearningGateway):
        self.machine_learning_gateway = machine_learning_gateway

    def translate_diagnosis(self, diagnosis: str) -> str:
       
        return PROGNOSES_TRANSLATIONS.get(diagnosis, diagnosis)

    def execute(self, symptoms: Dict[str, bool]) -> str:
        symptom_values = [symptoms.get(symptom, False) for symptom in ALL_POSSIBLE_SYMPTOMS]
        prediction = self.machine_learning_gateway.predict(symptom_values)

        translated_diagnosis = self.translate_diagnosis(prediction)

        return translated_diagnosis