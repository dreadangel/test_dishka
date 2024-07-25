from abc import abstractmethod
from asyncio import Task


class TaskManagerInterface:
    """ Интерфейс менеджера задач """

    tasks: dict[str, Task]

    @abstractmethod
    def get_task_status(self, worker_uuid: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def cancel_task(self, worker_uuid: str) -> str:
        raise NotImplementedError()

