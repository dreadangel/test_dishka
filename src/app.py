from src.core.appication import Application
from src.infrastructure.HelloWorldModule.main import HelloWorld


async def main() -> None:

    try:
        hello_world_module = HelloWorld()
        application = Application(hello_world=hello_world_module)
        application.run()
    finally:
        ...
