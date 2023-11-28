"""Fixtures for the render module unit tests."""
import random
import string
from typing import List

import pytest
from geneweaver.core.enum import GeneIdentifier, Microarray, ScoreType, Species
from geneweaver.core.schema.batch import BatchUploadGeneset
from geneweaver.core.schema.gene import GeneValue
from geneweaver.core.schema.score import GenesetScoreType

random.seed(0)

MOCK_GENE_CHARACTERS = string.ascii_letters + string.digits + "-_"


def mock_gene_values(n: int) -> List[GeneValue]:
    """Generate N mock gene values instances.

    :param n: The number of mock gene values to generate.

    :return: A list of mock gene values.
    """
    return [
        GeneValue(
            symbol="".join(random.choice(MOCK_GENE_CHARACTERS) for _ in range(10)),
            value=random.uniform(-2, 2),
        )
        for _ in range(n)
    ]


MOCK_GENE_VALUES = mock_gene_values(500)


@pytest.fixture(
    scope="session",
    params=[MOCK_GENE_VALUES[i : i + 10] for i in range(0, len(MOCK_GENE_VALUES), 10)],
)
def mock_gene_value_list(request):
    """Return a list of mock gene value instances."""
    return request.param


@pytest.fixture(scope="session", params=MOCK_GENE_VALUES)
def mock_gene_value(request) -> GeneValue:
    """Return a single mock gene value instance."""
    return request.param


@pytest.fixture(scope="session", params=[s for s in Species])
def species(request) -> Species:
    """Return a species enum value."""
    return request.param


@pytest.fixture(scope="session", params=[g for g in GeneIdentifier])
def gene_identifier(request) -> GeneIdentifier:
    """Return a gene identifier enum value."""
    return request.param


@pytest.fixture(scope="session", params=[m for m in Microarray])
def microarray(request) -> Microarray:
    """Return a microarray enum value."""
    return request.param


@pytest.fixture(scope="session", params=[s for s in ScoreType])
def score_type(request) -> ScoreType:
    """Return a score type enum value."""
    return request.param


@pytest.fixture(scope="session", params=[random.uniform(-2, 2) for _ in range(5)])
def geneset_score_type(score_type, request) -> GenesetScoreType:
    """Return a geneset score type instance."""
    return GenesetScoreType(score_type=score_type, threshold=request.param)


@pytest.fixture(scope="session")
def mock_batch_upload_geneset(
    geneset_score_type,
    species,
    gene_identifier,
) -> BatchUploadGeneset:
    """Return a mock batch upload geneset instance."""
    return BatchUploadGeneset(
        score=geneset_score_type,
        species=species,
        gene_id_type=gene_identifier,
        abbreviation="MOCK",
        name="Mock Geneset",
        description="Mock geneset for testing.",
        values=MOCK_GENE_VALUES,
    )


@pytest.fixture(scope="session")
def mock_empty_geneset() -> BatchUploadGeneset:
    """Return a mock batch upload geneset instance without any values."""
    return BatchUploadGeneset(
        score=GenesetScoreType(score_type=ScoreType.BINARY),
        species=Species.MUS_MUSCULUS,
        gene_id_type=GeneIdentifier.ENSEMBLE_GENE,
        abbreviation="None",
        name="None",
        description="None",
        values=[],
    )
