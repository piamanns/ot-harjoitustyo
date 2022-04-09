import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print(".env-file not found")

TF_PRESETS_FILENAME = os.getenv("TF_PRESETS_FILENAME") or "tf_presets.csv"
TF_PRESETS_PATH = os.path.join(dirname, "..", "data", TF_PRESETS_FILENAME)