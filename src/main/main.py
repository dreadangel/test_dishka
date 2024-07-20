import asyncio

from dishka import make_async_container

from src.core.appication import Application
from src.main.config import Config
from src.main.ioc import AdapterProvider


async def main() -> None:
    container = make_async_container(
        AdapterProvider(config=Config())
    )
    async with container():
        app = await container.get(Application)
        await app.run()


if __name__ == '__main__':
    asyncio.run(main())
