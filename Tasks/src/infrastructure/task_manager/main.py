from asyncio import Task

from Tasks.src.core.ports import TaskManagerInterface


class TaskManager(TaskManagerInterface):
    def __init__(self) -> None:
        self.tasks: dict[str, Task] = {}

    def get_task_status(self, worker_uuid: str) -> str:
        task = self.tasks.get(worker_uuid)
        if task is None:
            return "Task not found"
        if task.done():
            if task.cancelled():
                return "Cancelled"
            if task.exception() is not None:
                return "Failed"
            return "Completed"
        return "Running"

    def cancel_task(self, worker_uuid: str) -> str:
        task = self.tasks.get(worker_uuid)
        if task is None:
            return "Task not found"
        if not task.done():
            task.cancel()
            return "Cancelled"
        return "Failed"
