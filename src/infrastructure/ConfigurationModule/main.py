from src.main.config import Config


class ConfigurationModule:
    def __init__(self, config: Config) -> None:
        self.data = config.configuration_module.some_data
