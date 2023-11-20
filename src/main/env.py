import os 
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.environ.get('MODEL_PATH', 'model.pkl')
LABEL_ENCODER_PATH = os.environ.get('LABEL_ENCODER_PATH', 'encoder.pkl')
PORT = os.environ.get('PORT', 5000)
HOST = os.environ.get('HOST', '0.0.0.0')
DEBUG = os.environ.get('DEBUG', False)

envs = {
    'MODEL_PATH': MODEL_PATH,
    'LABEL_ENCODER_PATH': LABEL_ENCODER_PATH,
    'PORT': int(PORT),
    'HOST': HOST,
    'DEBUG': bool(DEBUG)
}