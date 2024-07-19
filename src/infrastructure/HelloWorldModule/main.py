from src.core.ports.helloworldport import HelloWorldInterface


class HelloWorld(HelloWorldInterface):
    def __init__(self, addt_text: str) -> None:
        self.text = f'Hello world! {addt_text}'

    async def hello_world(self) -> None:
        print(self.text)
