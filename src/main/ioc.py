from dishka import Provider, Scope, provide

from src.core.appication import Application
from src.core.ports.helloworldport import HelloWorldInterface
from src.infrastructure.HelloWorldModule.main import HelloWorld


class AdapterProvider(Provider):
    _provide_hello_world = provide(source=HelloWorld, provides=HelloWorldInterface, scope=Scope.APP)
    _provide_app = provide(source=Application, scope=Scope.APP)
