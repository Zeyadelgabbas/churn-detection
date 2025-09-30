from dotenv import load_dotenv
import os 


load_dotenv(override = True)

APP_NAME =os.getenv('APP_NAME')
VERSION = os.getenv("VERSION")
SECRET_KEY_TOKEN = os.getenv('SECRET_KEY_TOKEN')

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_FILE_PATH = os.path.join(PARENT_DIR,'Models')

PREPROCESSOR_FILE_PATH = os.path.join(MODELS_FILE_PATH,'preprocessor.pkl')
XGB_MODEL_PATH = os.path.join(MODELS_FILE_PATH,'xgb_tunned.pkl')
FORREST_MODEL_PATH = os.path.join(MODELS_FILE_PATH,'forest_tunned.pkl')