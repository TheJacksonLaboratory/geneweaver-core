"""Pydantic schema for defining score types."""
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from geneweaver.core.enum import ScoreType


class GenesetScoreType(BaseModel):
    """Pydantic schema for defining score types."""

    score_type: ScoreType
    threshold_low: Optional[float] = None
    threshold: float = 0.05

    def __str__(self) -> str:
        """Return a string representation of the score type."""
        name = self.score_type.name.title().replace("_", "-")
        if self.threshold_low:
            return f"{self.threshold_low} < {name} < {self.threshold}"
        return f"{name} < {self.threshold}"
