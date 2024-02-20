"""Pydantic schema for defining score types."""

from typing import Optional

from geneweaver.core.enum import ScoreType
from pydantic import BaseModel


class GenesetScoreType(BaseModel):
    """Pydantic schema for defining score types."""

    score_type: ScoreType
    threshold_low: Optional[float] = None
    threshold: float = 0.05

    def __str__(self: "GenesetScoreType") -> str:
        """Return a string representation of the score type."""
        name = self.score_type.name.title().replace("_", "-")
        if self.threshold_low:
            return f"{self.threshold_low} < {name} < {self.threshold}"
        return f"{name} < {self.threshold}"
