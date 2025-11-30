import base64
from pathlib import Path

CURRENT_FILE_PATH = Path(__file__).resolve()
PROJECT_ROOT_PATH = CURRENT_FILE_PATH.parent.parent.parent

ASSETS_DIRECTORY_PATH = PROJECT_ROOT_PATH / "assets"
STUB_IMAGE_PATH = ASSETS_DIRECTORY_PATH / "cat.png"

def generate_stub_image() -> str:
    if not STUB_IMAGE_PATH.exists():
        raise FileNotFoundError(f"Stub image not found: {STUB_IMAGE_PATH}")

    with open(STUB_IMAGE_PATH, "rb") as stub:
        stub_bytes = stub.read()

    base64_string = base64.b64encode(stub_bytes).decode("utf-8")

    return base64_string
