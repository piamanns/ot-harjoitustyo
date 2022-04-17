import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print(".env-file not found")

TF_PRESETS_FILENAME = os.getenv("TF_PRESETS_FILENAME") or "tf_presets.csv"
TF_PRESETS_PATH = os.path.join(dirname, "..", "data", TF_PRESETS_FILENAME)
METR_CLICK_FILENAME = os.getenv("METR_CLICK_FILENAME") or "click.wav"
METR_CLICK_PATH = os.path.join(dirname, "sounds", METR_CLICK_FILENAME)
TF_ICON_FILENAME = os.getenv("TF_ICON_FILENAME") or "icons8-tuning-fork-96.png"
TF_ICON_PATH = os.path.join(dirname, "images", TF_ICON_FILENAME)
METR_ICON_FILENAME = os.getenv("METR_ICON_FILENAME") or "icons8-metronome-96.png"
METR_ICON_PATH = os.path.join(dirname, "images", METR_ICON_FILENAME)
