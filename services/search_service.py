class SearchService:

    def __init__(self, collectors):
        self.collectors = collectors

    async def search(self):
        scholarships = []

        for collector in self.collectors:
            try:
                data = await collector.collect()
                scholarships.extend(data)

            except Exception as e:
                print(e)

        return scholarships
