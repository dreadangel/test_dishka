from src.core.ports.helloworldport import HelloWorldInterface


class Application:
    def __init__(self, hello_world: HelloWorldInterface) -> None:
        self.hello_world = hello_world

    async def run(self) -> None:
        await self.hello_world.hello_world()


