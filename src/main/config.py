import dataclasses


@dataclasses.dataclass(slots=True)
class ConfigConfigurationModule:
    some_data: str = 'some_value'


@dataclasses.dataclass(slots=True)
class ConfigHelloWorldModule:
    test_data: str


@dataclasses.dataclass(slots=True)
class Config:
    configuration_module = ConfigConfigurationModule()
    hello_world_module = ConfigHelloWorldModule()
