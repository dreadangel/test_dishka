from dishka import Provider, Scope, provide

from src.core.appication import Application
from src.core.ports.helloworldport import HelloWorldInterface
from src.infrastructure.New__HelloWorldModule.main import NewHelloWorld
from src.main.config import Config


class AdapterProvider(Provider):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return self.config

    _provide_hello_world = provide(source=NewHelloWorld, provides=HelloWorldInterface, scope=Scope.APP)
    _provide_app = provide(source=Application, scope=Scope.APP)
