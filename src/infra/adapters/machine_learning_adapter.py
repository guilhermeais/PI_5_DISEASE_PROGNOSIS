import joblib
from src.domain.gateways.machine_learning_gateway import MachineLearningGateway
import numpy as np

class MachineLearningAdapter(MachineLearningGateway):
    def __init__(self, model_path: str, label_encoder_path: str):
        self.model = joblib.load(model_path)
        self.label_encoder = joblib.load(label_encoder_path)

    def predict(self, symptoms: list[bool]) -> str:
        symptoms_array = np.array(symptoms).reshape(1, -1)
        prediction = self.model.predict(symptoms_array)
        predicted_label = self.label_encoder.inverse_transform(prediction)[0]
        return predicted_label
