from dishka import FromDishka

from src.core.ports.helloworldport import HelloWorldInterface


class Application:
    def __init__(self, hello_world: FromDishka[HelloWorldInterface]) -> None:
        self.hello_world = hello_world

    def run(self) -> None:
        self.hello_world.hello_world()


