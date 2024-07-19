from src.core.ports.helloworldport import HelloWorldInterface


class NewHelloWorld(HelloWorldInterface):
    def __init__(self) -> None:
        self.text = 'Hello world! New module'

    async def hello_world(self) -> None:
        print(self.text)
