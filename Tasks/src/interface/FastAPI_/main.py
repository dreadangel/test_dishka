from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from Tasks.src.interface.FastAPI_.routers import router
from Tasks.src.main.config import Config
from Tasks.src.main.ioc import AdaptersProvider


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    container = make_async_container(AdaptersProvider(config=Config()))
    setup_dishka(container, app)
    return app
