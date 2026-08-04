"""
docx_to_pdf.py — Converts an uploaded .docx resume to .pdf, for the
"Convert resume to PDF" option in the Hirelyzer landing page's chatbot
popover.

This is unrelated to the Groq/LLM chatbot in chatbot_llm.py — no AI model
is involved. Formatting a Word document into a PDF that keeps fonts,
tables, and layout intact needs an actual document engine, so this shells
out to headless LibreOffice:

    soffice --headless --convert-to pdf --outdir <dir> <file.docx>

Setup (Streamlit Community Cloud):
  - LibreOffice isn't installed by default. Add a `packages.txt` file at
    the repo root (Streamlit Cloud reads it for apt-level system
    packages, alongside requirements.txt for Python packages) containing:
        libreoffice-writer
    then reboot the app from the Cloud dashboard so the new system
    package actually gets installed.
  - No new Python dependency — this only uses the stdlib (subprocess,
    tempfile, pathlib, shutil).

Local/other hosts: just make sure `soffice` is on PATH
(`sudo apt install libreoffice-writer` on Debian/Ubuntu,
`brew install libreoffice` on macOS).
"""

import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional, Tuple

CONVERT_TIMEOUT_SECONDS = 60
MAX_UPLOAD_BYTES = 8 * 1024 * 1024   # 8 MB — resumes are small; guards against abuse/slow conversions


def soffice_available() -> bool:
    """
    Cheap presence check so the UI can show a clear "not set up yet"
    message instead of failing at conversion time with a confusing error.
    """
    return shutil.which("soffice") is not None


def convert_docx_to_pdf(file_bytes: bytes, original_filename: str) -> Tuple[Optional[bytes], Optional[str]]:
    """
    Converts a .docx file (as bytes) to .pdf (as bytes) via headless
    LibreOffice.

    Returns (pdf_bytes, error_message) — exactly one of the two is None.
    Never raises; every failure path is reported through error_message so
    callers can just check `if err:` and show it.
    """
    if not soffice_available():
        return None, "PDF conversion isn't set up on this server yet (LibreOffice not found)."

    if Path(original_filename).suffix.lower() != ".docx":
        return None, "Please upload a .docx (Word) file."

    if len(file_bytes) > MAX_UPLOAD_BYTES:
        mb = MAX_UPLOAD_BYTES // (1024 * 1024)
        return None, f"That file is too large — please upload something under {mb} MB."

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_in = Path(tmpdir) / "resume.docx"
        tmp_in.write_bytes(file_bytes)

        try:
            result = subprocess.run(
                [
                    "soffice", "--headless", "--norestore",
                    "--convert-to", "pdf", "--outdir", tmpdir, str(tmp_in),
                ],
                capture_output=True,
                timeout=CONVERT_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return None, "Conversion timed out — please try again."
        except Exception as e:
            return None, f"Couldn't start the conversion ({e})."

        tmp_out = Path(tmpdir) / "resume.pdf"
        if result.returncode != 0 or not tmp_out.exists():
            stderr = (result.stderr or b"").decode("utf-8", errors="ignore").strip()
            detail = f": {stderr}" if stderr else "."
            return None, f"Conversion failed{detail}"

        return tmp_out.read_bytes(), None
