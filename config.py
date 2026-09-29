import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DRIVERS_DIR = BASE_DIR / "drivers"
DATA_DIR = BASE_DIR / "data"
for d in [DRIVERS_DIR, DATA_DIR]:
    d.mkdir(parents=True, exist_ok=True)

CHATGPT_URL = "https://chatgpt.com/"
CHATGPT_TEXTAREA_ID = "prompt-textarea"
CHATGPT_SEND_BUTTON_SELECTOR = "[data-testid='send-button']"

_local_app_data = os.environ.get("LOCALAPPDATA", r"C:\Users\Default\AppData\Local")
EDGE_USER_DATA_DIR = os.path.join(_local_app_data, "Microsoft", "Edge", "User Data")
EDGE_PROFILE_DIR = "Default"
DEFAULT_DRIVER_PATH = DRIVERS_DIR / "msedgedriver.exe"

# Rutas externas: deben configurarse en el entorno local.
PATH_INSTRUCCIONES = os.environ.get("TRANSCRIPTOR_INSTRUCCIONES", str(BASE_DIR / "inputs" / "prompt_transcripcion.txt"))
PATH_WHISPER_DEFAULT = os.environ.get("TRANSCRIPTOR_WHISPER", str(BASE_DIR / "inputs" / "Texto de Whisper.txt"))
