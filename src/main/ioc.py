from dishka import Provider, Scope, provide

from src.core.appication import Application
from src.core.ports.helloworldport import HelloWorldInterface
from src.infrastructure.New__HelloWorldModule.main import NewHelloWorld


class AdapterProvider(Provider):
    _provide_hello_world = provide(source=NewHelloWorld, provides=HelloWorldInterface, scope=Scope.APP)
    _provide_app = provide(source=Application, scope=Scope.APP)
