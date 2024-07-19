from abc import abstractmethod
from typing import Protocol


class HelloWorldInterface(Protocol):
    @abstractmethod
    async def hello_world(self) -> None:
        raise NotImplementedError
