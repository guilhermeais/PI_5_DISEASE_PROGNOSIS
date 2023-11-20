import os 
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.environ.get('MODEL_PATH', 'model.pkl')
LABEL_ENCODER_PATH = os.environ.get('LABEL_ENCODER_PATH', 'encoder.pkl')

envs = {
    'MODEL_PATH': MODEL_PATH,
    'LABEL_ENCODER_PATH': LABEL_ENCODER_PATH
}