"""Module for defining schemas for batch endpoints."""

# ruff: noqa: N805, ANN001, ANN101, ANN401
from typing import Any, List, Optional, Type, Union

from geneweaver.core.enum import GeneIdentifierInt, MicroarrayInt, SpeciesInt
from geneweaver.core.parse.score import parse_score
from geneweaver.core.schema.gene import GeneValue
from geneweaver.core.schema.messages import MessageResponse
from geneweaver.core.schema.score import GenesetScoreType
from pydantic import BaseModel, field_validator, model_validator
from typing_extensions import Self

# Header characters which DO NOT need to be space separated.
HEADER_CHARACTERS = {
    ":": "abbreviation",
    "=": "name",
    "+": "description",
    "@": "species",
    "!": "score",
    "%": "gene_id_type",
    "~": "ontology",
}

# Header characters which DO need to be space separated. This is because these
# characters can also be seen in the values section of the batch file.
SPACE_SEPARATED_HEADER_CHARACTERS = {
    "P": "pubmed_id",
    "A": "private",
    "T": "curation_id",
    "U": "user_id",
    "D": "attribution_id",
}

# Characters which should be ignored in the batch file.
IGNORE_CHARACTERS = {
    "#": "comment",
    " ": "space",
}

# Batch characters
# TODO: Switch to this 3.9+ syntax.
# For now, we use the 3.5+ syntax.
CHAR_MAP = {
    **HEADER_CHARACTERS,
    **SPACE_SEPARATED_HEADER_CHARACTERS,
    **IGNORE_CHARACTERS,
}

# Inverse character map for converting from header name to character.
INV_CHAR_MAP = {v: k for k, v in CHAR_MAP.items()}

# Characters denoting required header information for all genesets.
REQUIRED_HEADERS = (":", "=", "+")


GenesetValueInput = GeneValue


class BatchResponse(BaseModel):
    """Class for defining a response containing batch results."""

    genesets: List[int]
    messages: MessageResponse


class GenesetValue(BaseModel):
    """Class for defining a geneset value as processed."""

    ode_gene_id: str
    value: float
    ode_ref_id: str
    threshold: bool


class BatchUploadGeneset(BaseModel):
    """Class for defining a geneset uploaded using a batch upload file."""

    score: GenesetScoreType
    species: SpeciesInt
    gene_id_type: Union[GeneIdentifierInt, MicroarrayInt]
    pubmed_id: Optional[str] = None
    private: bool = True
    curation_id: Optional[int] = None
    abbreviation: str
    name: str
    description: str = ""
    values: List[GeneValue]

    @field_validator("species", mode="before")
    @classmethod
    def initialize_species(cls: Type["BatchUploadGeneset"], v: Any) -> SpeciesInt:
        """Initialize species."""
        if isinstance(v, SpeciesInt):
            return v
        elif isinstance(v, str):
            return SpeciesInt[v.replace(" ", "_").upper()]
        return SpeciesInt(v)

    @field_validator("gene_id_type", mode="before")
    @classmethod
    def initialize_gene_id_type(
        cls: Type["BatchUploadGeneset"], v: Any
    ) -> Union[GeneIdentifierInt, MicroarrayInt]:
        """Initialize gene id type."""
        if isinstance(v, GeneIdentifierInt) or isinstance(v, MicroarrayInt):
            return v
        try:
            if isinstance(v, str):
                return GeneIdentifierInt[v.replace(" ", "_").upper()]
            return GeneIdentifierInt(v)
        except KeyError:
            if isinstance(v, str):
                return MicroarrayInt[
                    v.upper().replace("MICROARRAY", "").strip().replace(" ", "_")
                ]
            return MicroarrayInt(v)

    @field_validator("score", mode="before")
    @classmethod
    def initialize_score(cls: Type["BatchUploadGeneset"], v: Any) -> GenesetScoreType:
        """Initialize score type."""
        if isinstance(v, GenesetScoreType):
            return v
        elif isinstance(v, dict):
            return GenesetScoreType(**v)
        return parse_score(v)

    @field_validator("private", mode="before")
    @classmethod
    def private_to_bool(cls: Type["BatchUploadGeneset"], v: Any) -> bool:
        """Convert private str to bool."""
        if isinstance(v, bool):
            return v
        return v.lower() != "public"

    @model_validator(mode="after")
    def curation_id_to_int(self) -> Self:
        """Initialize curation id based on `private` value."""
        if not self.curation_id:
            # If the geneset is private, it should be set to have
            # curation tier 5, otherwise it should be set to have
            # curation tier 4.
            # It should default to private if not specified.
            self.curation_id = 5 if self.private else 4
        return self
