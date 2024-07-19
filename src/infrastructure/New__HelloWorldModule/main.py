from src.core.ports.helloworldport import HelloWorldInterface


class NewHelloWorld(HelloWorldInterface):
    def __init__(self, addt_text: str) -> None:
        self.text = f'Hello world! New module {addt_text}'

    async def hello_world(self) -> None:
        print(self.text)
