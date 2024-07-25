import structlog

from Tasks.src.main.config import Config

logger: structlog.BoundLogger = structlog.get_logger("Worker")


class Worker:
    def __init__(self, config: Config) -> None:
        self.status = False
        self.name: str = config.worker_name

    async def stat(self) -> None:
        self.status = True
        await logger.adebug("Worker started", worker_name=self.name)

    async def stop(self) -> None:
        self.status = False
        await logger.adebug("Worker stopped", worker_name=self.name)

    async def status(self) -> bool:
        return self.status
