from abc import ABC, abstractmethod
class BaseCollector(ABC):
    name="base"
    @abstractmethod
    async def collect(self): ...
