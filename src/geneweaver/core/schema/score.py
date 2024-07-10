"""Pydantic schema for defining score types."""

# ruff: noqa: N805

from typing import Optional

from geneweaver.core.enum import ScoreType
from pydantic import BaseModel, model_validator
from typing_extensions import Self


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

    @model_validator(mode="after")
    def threshold_low_must_be_less_than_threshold(self) -> Self:
        """Threshold low must be less than threshold."""
        if self.threshold_low is not None and self.threshold_low > self.threshold:
            raise ValueError("threshold_low must be less than threshold")
        return self

    @model_validator(mode="after")
    def threshold_low_correlation_and_effect_only(self) -> Self:
        """Threshold low should only be set for correlation and effect score types."""
        if self.threshold_low is not None and self.score_type not in [
            ScoreType.CORRELATION,
            ScoreType.EFFECT,
        ]:
            raise ValueError(
                "threshold_low should only be set for "
                "correlation and effect score types"
            )
        return self
