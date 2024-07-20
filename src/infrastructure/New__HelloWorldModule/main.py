from src.core.ports.helloworldport import HelloWorldInterface
from src.main.config import Config


class NewHelloWorld(HelloWorldInterface):
    def __init__(self, config: Config) -> None:
        self.text = f'Hello world! New module {config.hello_world_module.test_data}'

    async def hello_world(self) -> None:
        print(self.text)
