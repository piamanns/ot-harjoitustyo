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
METR_CLICK_UP_FILENAME = os.getenv("METR_CLICK_UP_FILENAME") or "click.wav"
METR_CLICK_UP_PATH = os.path.join(dirname, "sounds", METR_CLICK_UP_FILENAME)
TF_ICON_FILENAME = os.getenv("TF_ICON_FILENAME") or "icons8-tuning-fork-96.png"
TF_ICON_PATH = os.path.join(dirname, "images", TF_ICON_FILENAME)
METR_ICON_FILENAME = os.getenv("METR_ICON_FILENAME") or "icons8-metronome-96.png"
METR_ICON_PATH = os.path.join(dirname, "images", METR_ICON_FILENAME)

TF_FREQ_MAX = os.getenv("TF_FREQ_MAX") or 8000
TF_FREQ_MIN =  os.getenv("TF_FREQ_MIN") or 20
METR_BPM_MAX = os.getenv("METR_BPM_MAX") or 500
METR_BPM_MIN = os.getenv("METR_BPM_MIN") or 1
METR_BEATS_MAX = os.getenv("METR_BEATS_MAX") or 12
METR_BEATS_MIN = os.getenv("METR_BEATS_MIN") or 1
