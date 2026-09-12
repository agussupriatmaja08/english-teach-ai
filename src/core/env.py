import os
from dotenv import load_dotenv
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent  # ../src
INSTRUCTIONS_DIR = SRC_DIR / "agents" / "instructions"
DOCS_DIR = SRC_DIR / "docs"
OUTPUT_DIR = SRC_DIR / "output"

from pathlib import Path

# p = Path(__file__).resolve()
# print("file:", p)
# print("parent:", p.parent)
# print("parent.parent:", p.parent.parent)

load_dotenv()


def _required_env(name: str) -> str:
    """Ambil env wajib. apabila gagal, tampilkan pesan error"""
    value = os.getenv(name)

    if not value:
        raise RuntimeError("Value belum di-set")

    return value


GEMINI_API_KEY = _required_env("GEMINI_API_KEY")
GEMINI_MODEL = _required_env("GEMINI_MODEL")
GEMINI_MODEL_TTS = _required_env("GEMINI_MODEL_TTS")

SUPABASE_URL = _required_env("SUPABASE_URL")
SUPABASE_KEY = _required_env("SUPABASE_KEY")
