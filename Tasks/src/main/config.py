import dataclasses


@dataclasses.dataclass(slots=True)
class Config:
    worker_name = "TestWorker"
