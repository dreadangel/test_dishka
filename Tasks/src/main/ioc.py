from dishka import Provider, Scope, provide

from Tasks.src.core.applications.worker import Worker
from Tasks.src.main.config import Config


class AdaptersProvider(Provider):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return self.config

    _provide_worker = provide(source=Worker, scope=Scope.APP)
