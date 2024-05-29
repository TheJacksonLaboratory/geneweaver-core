"""Pydantic schema for defining score types."""

# ruff: noqa: N805

from typing import Optional

from geneweaver.core.enum import ScoreType
from pydantic import BaseModel, validator


class GenesetScoreType(BaseModel):
    """Pydantic schema for defining score types."""

    score_type: ScoreType
    threshold: float = 0.05
    threshold_low: Optional[float] = None

    def __str__(self: "GenesetScoreType") -> str:
        """Return a string representation of the score type."""
        name = self.score_type.name.title().replace("_", "-")
        if self.threshold_low:
            return f"{self.threshold_low} < {name} < {self.threshold}"
        return f"{name} < {self.threshold}"

    def threshold_as_db_string(self) -> str:
        """Return a string representation of the score type for the database."""
        if self.threshold_low is not None:
            return f"{self.threshold_low},{self.threshold}"
        else:
            return str(self.threshold)

    @validator("threshold_low")
    def threshold_low_must_be_less_than_threshold(
        cls, v: Optional[float], values: dict
    ) -> Optional[float]:
        """Threshold low must be less than threshold."""
        if v is not None and v > values.get("threshold"):
            raise ValueError("threshold_low must be less than threshold")
        return v

    @validator("threshold_low")
    def threshold_low_correlation_and_effect_only(
        cls, v: Optional[float], values: dict
    ) -> Optional[float]:
        """Threshold low should only be set for correlation and effect score types."""
        if v is not None and values.get("score_type") not in [
            ScoreType.CORRELATION,
            ScoreType.EFFECT,
        ]:
            raise ValueError(
                "threshold_low should only be set for "
                "correlation and effect score types"
            )
        return v
