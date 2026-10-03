from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Set

@dataclass
class Movie:
    id: str
    title: str
    year: Optional[int]
    avg_rating: Optional[float]

    attori: list = field(default_factory=list)


    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Movie):
            return self.id == other.id
        return False

    def __repr__(self):
        return f"{self.title} ({self.year if self.year is not None else 'N/D'})"