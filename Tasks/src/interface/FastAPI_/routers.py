import asyncio
import uuid
from asyncio import Task

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from Tasks.src.core.applications.worker import Worker
from Tasks.src.core.ports import TaskManagerInterface

router = APIRouter(route_class=DishkaRoute)


@router.get("/ping")
async def ping() -> str:
    return "pong"


@router.post("/start")
async def worker_start(*, task_manager: FromDishka[TaskManagerInterface], worker: FromDishka[Worker]) -> str:
    worker_uuid: str = uuid.uuid4().hex
    task: Task = asyncio.create_task(worker.run())
    task_manager.tasks[worker_uuid] = task
    return worker_uuid


@router.post("/stop")
async def worker_stop(worker_uuid: str, *, task_manager: FromDishka[TaskManagerInterface]) -> str:
    return task_manager.cancel_task(worker_uuid)


@router.get("/status")
async def worker_status(worker_uuid: str, *, task_manager: FromDishka[TaskManagerInterface]) -> str:
    return task_manager.get_task_status(worker_uuid)



