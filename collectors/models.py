from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Scholarship:

    title: str

    institution: str

    country: str

    level: str

    coverage: str

    url: str

    deadline: Optional[date]

    colombians: bool = True

    minimum_age: int = 16

    language: str = "English"

    score: int = 0
