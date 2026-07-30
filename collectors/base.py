from abc import ABC

class BaseCollector(ABC):

    name = ""

    country = ""

    source = ""

    async def collect(self):

        raise NotImplementedError

    async def normalize(self, scholarship):

        return scholarship

    def validate(self, scholarship):

        if scholarship.url == "":
            return False

        return True
