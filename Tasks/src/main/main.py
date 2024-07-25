import anyio
import uvicorn

from Tasks.src.interface.FastAPI_.main import create_app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="127.0.0.1", port=8000, lifespan="on")
