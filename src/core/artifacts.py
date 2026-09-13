import contextvars
from typing import Optional, TypedDict, Literal


class Artifact(TypedDict):
    path: str
    kind: str  # kind : audio | document
    caption: Optional[str]


_artifact: contextvars.ContextVar[Optional[list[Artifact]]] = contextvars.ContextVar(
    "artifacts", default=None
)


def start() -> None:
    _artifact.set([])  #  menyiapkan nilai kosong


# catatan : nama fungsi yang berisikan _ diawal menandakan fungsi tidak bisa diakses di luar module


def add(
    path: str, kind: Literal["audio", "document"], caption: Optional[str] = None
) -> None:
    """Catat satu artifact untuk dikirim oleh layer pengiriman (CLI/Telegram)"""
    bucket = _artifact.get()

    if bucket is None:
        return

    bucket.append({"path": path, "kind": kind, "caption": caption})


def collect() -> list[Artifact]:
    """Ambil semua list artifact yang terkumpul pada request ini"""
    return _artifact.get() or []
