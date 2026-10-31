# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/atomic.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""Whole-file writes: a reader (a check, a test, an editor) sees the old file or the new one, never half of it.

The generators rewrite READMEs and data files that other processes read at the same time (a check running in parallel with a regeneration). Writing
in place truncates the file first, so such a reader could see an empty or cut file. The content goes to a temporary file in the same folder and is
then moved over the target in one step. On Windows the move can be refused for a moment while a reader holds the file open, so it is retried briefly.
"""
from __future__ import annotations

import os
import tempfile
import time
from pathlib import Path

_ATTEMPTS = 40
_PAUSE_SECONDS = 0.05


def write_bytes(path: Path, data: bytes) -> None:
    """Replaces `path` with `data` in one step; the temporary file is removed if anything fails."""
    path = Path(path)
    handle, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        for attempt in range(_ATTEMPTS):
            try:
                os.replace(temporary, path)
                return
            except PermissionError:
                if attempt == _ATTEMPTS - 1:
                    raise
                time.sleep(_PAUSE_SECONDS)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_text(path: Path, text: str, newline: str | None = "\n") -> None:
    """Like Path.write_text with UTF-8; `newline` is what "\n" becomes (default: left as "\n")."""
    data = text if newline in (None, "\n", "") else text.replace("\n", newline)
    write_bytes(path, data.encode("utf-8"))
