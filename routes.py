from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h1>FitBuddy-AI</h1>
    <p>Your AI-powered fitness and wellness app.</p>
    """