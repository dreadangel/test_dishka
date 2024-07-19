from src.infrastructure.HelloWorldModule.main import HelloWorld


class Application:
    def __init__(self, hello_world: HelloWorld) -> None:
        self.hello_world = hello_world

    def run(self) -> None:
        self.hello_world.hello_world()


