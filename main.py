from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .database import init_db
from .routes import router

BASE_DIR = Path(__file__).resolve().parent
@asynccontextmanager
async def lifespan(app: FastAPI):

    Path("data").mkdir(
        exist_ok=True
    )

    init_db()

    yield


app = FastAPI(

    title=settings.app_name,

    description=(
        "AI-powered 7-day fitness and "
        "wellness plan generator."
    ),

    version="1.0.0",

    lifespan=lifespan
)


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


app.include_router(router)