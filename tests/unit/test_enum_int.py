"""Test the enum module."""

from enum import Enum, IntEnum

import pytest
from geneweaver.core.enum import (
    AdminLevelInt,
    CurationAssignmentInt,
    GeneIdentifierInt,
    GenesetAccess,
    MicroarrayInt,
    ScoreType,
    ScoreTypeInt,
    SpeciesInt,
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
    """Test the CurationAssignmentInt enum."""
    assert getattr(CurationAssignmentInt, attribute) == expected


@pytest.mark.parametrize(
    ("int_value", "expected"),
    [
        (1, CurationAssignmentInt.UNASSIGNED),
        (2, CurationAssignmentInt.ASSIGNED),
        (3, CurationAssignmentInt.READY_FOR_REVIEW),
        (4, CurationAssignmentInt.REVIEWED),
        (5, CurationAssignmentInt.APPROVED),
    ],
)
def test_curation_assignment_from_int(
    int_value: int, expected: CurationAssignmentInt
) -> None:
    """Test the CurationAssignmentInt enum creation from an int."""
    assert CurationAssignmentInt(int_value) == expected


@pytest.mark.parametrize(
    ("attribute", "expected"), [("PRIVATE", "private"), ("PUBLIC", "public")]
)
def test_geneset_access(attribute: str, expected: str) -> None:
    """Test the GenesetAccess enum."""
    assert getattr(GenesetAccess, attribute).value == expected


def test_geneset_access_from_string() -> None:
    """Test the GenesetAccess enum creation from a string."""
    assert GenesetAccess("private") == GenesetAccess.PRIVATE
    assert GenesetAccess("public") == GenesetAccess.PUBLIC


def test_geneset_score_type() -> None:
    """Test the GenesetScoreTypeInt enum."""
    assert ScoreTypeInt.P_VALUE == 1
    assert ScoreTypeInt.Q_VALUE == 2
    assert ScoreTypeInt.BINARY == 3
    assert ScoreTypeInt.CORRELATION == 4
    assert ScoreTypeInt.EFFECT == 5


def test_geneset_score_type_from_int() -> None:
    """Test the GenesetScoreTypeInt enum creation from an int."""
    assert ScoreTypeInt(1) == ScoreTypeInt.P_VALUE
    assert ScoreTypeInt(2) == ScoreTypeInt.Q_VALUE
    assert ScoreTypeInt(3) == ScoreTypeInt.BINARY
    assert ScoreTypeInt(4) == ScoreTypeInt.CORRELATION
    assert ScoreTypeInt(5) == ScoreTypeInt.EFFECT


def test_geneset_score_type_str() -> None:
    """Test the ScoreTypeInt enum."""
    assert str(ScoreType.P_VALUE) == "p-value"
    assert str(ScoreType.Q_VALUE) == "q-value"
    assert str(ScoreType.BINARY) == "binary"
    assert str(ScoreType.CORRELATION) == "correlation"
    assert str(ScoreType.EFFECT) == "effect"


def test_geneset_score_type_str_from_string() -> None:
    """Test the ScoreTypeInt enum creation from a string."""
    assert ScoreType("p-value") == ScoreType.P_VALUE
    assert ScoreType("q-value") == ScoreType.Q_VALUE
    assert ScoreType("binary") == ScoreType.BINARY
    assert ScoreType("correlation") == ScoreType.CORRELATION
    assert ScoreType("effect") == ScoreType.EFFECT


@pytest.mark.parametrize(
    "enum_class",
    [
        CurationAssignmentInt,
        ScoreTypeInt,
        AdminLevelInt,
        SpeciesInt,
        GeneIdentifierInt,
        MicroarrayInt,
    ],
)
def test_is_int_enum(enum_class):
    """Test that Integer Enums are defined as IntEnum."""
    assert issubclass(enum_class, int)
    assert issubclass(enum_class, Enum)
    assert issubclass(enum_class, IntEnum)
