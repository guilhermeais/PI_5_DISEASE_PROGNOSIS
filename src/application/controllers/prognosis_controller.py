from flask import Flask, request, jsonify
from src.domain.use_cases.prognosis_use_case import PrognosisUseCase
from src.domain.entities.symptoms import ALL_POSSIBLE_SYMPTOMS_PT_BR
from src.infra.adapters.machine_learning_adapter import MachineLearningAdapter
from src.main.env import envs

app = Flask(__name__)
machine_learning_gateway = MachineLearningAdapter(envs.get('MODEL_PATH'), envs.get('LABEL_ENCODER_PATH'))


@app.route('/prognosis', methods=['POST'])
def predict_prognosis():
    data = request.json
    prognosis_use_case = PrognosisUseCase(machine_learning_gateway=machine_learning_gateway)
    result = prognosis_use_case.execute(data)
    return jsonify({"prognosis": result})


@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({'symptoms': ALL_POSSIBLE_SYMPTOMS_PT_BR})