from abc import ABC
from typing import List

from app.collectors.models import Scholarship


class BaseCollector(ABC):

    name = ""

    async def collect(self) -> List[Scholarship]:
        raise NotImplementedError

    def validate(self, scholarship: Scholarship) -> bool:

        if scholarship.title == "":
            return False

        if scholarship.url == "":
            return False

        return True
