import asyncio

import structlog

from Tasks.src.main.config import Config

logger: structlog.BoundLogger = structlog.get_logger("Worker")


class Worker:
    def __init__(self, config: Config) -> None:
        self.status = False
        self.name: str = config.worker_name

    async def run(self) -> None:
        self.status = True
        await logger.adebug("Worker started", worker_name=self.name)
        await asyncio.sleep(10)
        await logger.adebug("Worker finish", worker_name=self.name)
