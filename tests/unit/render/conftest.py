"""Fixtures for the render module unit tests."""
import random
import string
from typing import List, Union

import pytest
from geneweaver.core.enum import GeneIdentifier, Microarray, ScoreType, Species
from geneweaver.core.schema.batch import BatchUploadGeneset
from geneweaver.core.schema.gene import GeneValue
from geneweaver.core.schema.score import GenesetScoreType

random.seed(0)

MOCK_GENE_CHARACTERS = string.ascii_letters + string.digits + "-_"
MOCK_FLOAT_VALUES = [0.55, 0.136, 0.01, 0.99, -0.53]
SCORE_TYPES = [s for s in ScoreType]
GENE_IDS = [g for g in GeneIdentifier]
MICROARRAYS = [m for m in Microarray]
SPECIES = [s for s in Species]
ALL_GENE_IDS = GENE_IDS + MICROARRAYS
ONE_GENE_ID_ONE_MICROARRAY = [
    GeneIdentifier.ENSEMBLE_GENE,
    Microarray.AFFYMETRIX_MOUSE_EXPRESSION_430_SET,
]


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
MOCK_GENE_VALUE_LISTS = [
    MOCK_GENE_VALUES[i : i + 10] for i in range(0, len(MOCK_GENE_VALUES), 10)
]


@pytest.fixture(scope="session", params=MOCK_GENE_VALUE_LISTS)
def mock_gene_value_list(request):
    """Return a list of mock gene value instances."""
    return request.param


@pytest.fixture(params=MOCK_GENE_VALUES)
def mock_gene_value(request) -> GeneValue:
    """Return a single mock gene value instance."""
    return request.param


@pytest.fixture(params=SPECIES)
def species(request) -> Species:
    """Return a species enum value."""
    return request.param


@pytest.fixture(params=GENE_IDS)
def gene_identifier(request) -> GeneIdentifier:
    """Return a gene identifier enum value."""
    return request.param


@pytest.fixture(params=MICROARRAYS)
def microarray(request) -> Microarray:
    """Return a microarray enum value."""
    return request.param


@pytest.fixture(params=ALL_GENE_IDS)
def any_gene_identifier(request) -> Union[GeneIdentifier, Microarray]:
    """Return a gene identifier or microarray enum value."""
    return request.param


@pytest.fixture(params=ONE_GENE_ID_ONE_MICROARRAY)
def one_gene_id_one_microarray(request) -> Union[GeneIdentifier, Microarray]:
    """Return a gene identifier or microarray enum value."""
    return request.param


@pytest.fixture(params=SCORE_TYPES)
def score_type(request) -> ScoreType:
    """Return a score type enum value."""
    return request.param


@pytest.fixture(params=MOCK_FLOAT_VALUES)
def geneset_score_type(score_type, request) -> GenesetScoreType:
    """Return a geneset score type instance."""
    return GenesetScoreType(score_type=score_type, threshold=request.param)


@pytest.fixture()
def mock_batch_upload_geneset_all_species_scores(
    species, geneset_score_type
) -> BatchUploadGeneset:
    """Return a mock batch upload geneset instance."""
    return BatchUploadGeneset(
        score=geneset_score_type,
        species=species,
        gene_id_type=GeneIdentifier.ENSEMBLE_GENE,
        abbreviation="MOCK",
        name="Mock Species Geneset",
        description="Mock geneset for testing.",
        values=MOCK_GENE_VALUES,
    )


@pytest.fixture()
def mock_batch_upload_geneset_all_combinations(
    geneset_score_type,
    species,
    any_gene_identifier,
) -> BatchUploadGeneset:
    """Return a mock batch upload geneset instance."""
    return BatchUploadGeneset(
        score=geneset_score_type,
        species=species,
        gene_id_type=any_gene_identifier,
        abbreviation="MOCK",
        name="Mock Geneset",
        description="Mock geneset for testing.",
        values=MOCK_GENE_VALUES,
    )


@pytest.fixture()
def mock_batch_upload_geneset_one_gene_id_one_microarray(
    geneset_score_type,
    species,
    one_gene_id_one_microarray,
) -> BatchUploadGeneset:
    """Return a mock batch upload geneset instance."""
    return BatchUploadGeneset(
        score=geneset_score_type,
        species=species,
        gene_id_type=one_gene_id_one_microarray,
        abbreviation="MOCK",
        name="Mock Geneset",
        description="Mock geneset for testing.",
        values=MOCK_GENE_VALUES,
    )


@pytest.fixture()
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
