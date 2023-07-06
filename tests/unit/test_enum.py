"""Test the enum module."""
import pytest
from geneweaver.core.enum import (
    CurationAssignment,
    GenesetAccess,
    GenesetScoreType,
    GenesetScoreTypeStr,
)


@pytest.mark.parametrize(
    ("attribute", "expected"),
    [
        ("UNASSIGNED", 1),
        ("ASSIGNED", 2),
        ("READY_FOR_REVIEW", 3),
        ("REVIEWED", 4),
        ("APPROVED", 5),
    ],
)
def test_curation_assignment(attribute: str, expected: int) -> None:
    """Test the CurationAssignment enum."""
    assert getattr(CurationAssignment, attribute) == expected


@pytest.mark.parametrize(
    ("int_value", "expected"),
    [
        (1, CurationAssignment.UNASSIGNED),
        (2, CurationAssignment.ASSIGNED),
        (3, CurationAssignment.READY_FOR_REVIEW),
        (4, CurationAssignment.REVIEWED),
        (5, CurationAssignment.APPROVED),
    ],
)
def test_curation_assignment_from_int(
    int_value: int, expected: CurationAssignment
) -> None:
    """Test the CurationAssignment enum creation from an int."""
    assert CurationAssignment(int_value) == expected


@pytest.mark.parametrize(
    ("attribute", "expected"), [("PRIVATE", "private"), ("PUBLIC", "public")]
)
def test_geneset_access(attribute: str, expected: str) -> None:
    """Test the GenesetAccess enum."""
    assert getattr(GenesetAccess, attribute) == expected


def test_geneset_access_from_string() -> None:
    """Test the GenesetAccess enum creation from a string."""
    assert GenesetAccess("private") == GenesetAccess.PRIVATE
    assert GenesetAccess("public") == GenesetAccess.PUBLIC


def test_geneset_score_type() -> None:
    """Test the GenesetScoreType enum."""
    assert GenesetScoreType.P_VALUE == 1
    assert GenesetScoreType.Q_VALUE == 2
    assert GenesetScoreType.BINARY == 3
    assert GenesetScoreType.CORRELATION == 4
    assert GenesetScoreType.EFFECT == 5


def test_geneset_score_type_from_int() -> None:
    """Test the GenesetScoreType enum creation from an int."""
    assert GenesetScoreType(1) == GenesetScoreType.P_VALUE
    assert GenesetScoreType(2) == GenesetScoreType.Q_VALUE
    assert GenesetScoreType(3) == GenesetScoreType.BINARY
    assert GenesetScoreType(4) == GenesetScoreType.CORRELATION
    assert GenesetScoreType(5) == GenesetScoreType.EFFECT


def test_geneset_score_type_str() -> None:
    """Test the GenesetScoreTypeStr enum."""
    assert GenesetScoreTypeStr.P_VALUE == "p-value"
    assert GenesetScoreTypeStr.Q_VALUE == "q-value"
    assert GenesetScoreTypeStr.BINARY == "binary"
    assert GenesetScoreTypeStr.CORRELATION == "correlation"
    assert GenesetScoreTypeStr.EFFECT == "effect"


def test_geneset_score_type_str_from_string() -> None:
    """Test the GenesetScoreTypeStr enum creation from a string."""
    assert GenesetScoreTypeStr("p-value") == GenesetScoreTypeStr.P_VALUE
    assert GenesetScoreTypeStr("q-value") == GenesetScoreTypeStr.Q_VALUE
    assert GenesetScoreTypeStr("binary") == GenesetScoreTypeStr.BINARY
    assert GenesetScoreTypeStr("correlation") == GenesetScoreTypeStr.CORRELATION
    assert GenesetScoreTypeStr("effect") == GenesetScoreTypeStr.EFFECT
