import asyncio

from app.collectors.icetex import ICETEXCollector

from app.services.search_service import SearchService


async def run():

    collectors = [

        ICETEXCollector()

    ]

    service = SearchService(

        collectors

    )

    scholarships = await service.search()

    for scholarship in scholarships:

        print()

        print("==========")

        print(scholarship.title)

        print(scholarship.country)

        print(scholarship.coverage)

        print(scholarship.url)


if __name__ == "__main__":

    asyncio.run(run())
