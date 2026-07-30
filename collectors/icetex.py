from datetime import date

from app.collectors.base import BaseCollector
from app.collectors.models import Scholarship


class ICETEXCollector(BaseCollector):

    name = "ICETEX"

    async def collect(self):

        return [

            Scholarship(

                title="Programa de Becas Internacionales",

                institution="ICETEX",

                country="Canada",

                level="Bachelor",

                coverage="Full",

                deadline=date(2026,11,15),

                url="https://www.icetex.gov.co"

            )

        ]
