from typing import List

from app.collectors.models import Scholarship


class SearchService:

    def __init__(self, collectors):

        self.collectors = collectors

    async def search(self) -> List[Scholarship]:

        scholarships = []

        for collector in self.collectors:

            data = await collector.collect()

            scholarships.extend(data)

        return scholarships
