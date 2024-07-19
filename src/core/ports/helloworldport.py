from abc import abstractmethod
from typing import Protocol


class HelloWorldInterface(Protocol):
    @abstractmethod
    def hello_world(self) -> None:
        raise NotImplementedError
