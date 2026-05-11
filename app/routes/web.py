from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index():
    template_path = Path(__file__).resolve().parent.parent / "templates" / "index.html"
    return HTMLResponse(template_path.read_text(encoding="utf-8"))
