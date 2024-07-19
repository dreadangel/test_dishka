from dishka import Provider, Scope, provide

from src.core.ports.helloworldport import HelloWorldInterface


class AdapterProvider(Provider):
    scope = Scope.REQUEST

    product = provide(HelloWorldInterface)
