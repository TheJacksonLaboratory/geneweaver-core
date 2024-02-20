"""Test that Enum and IntEnum has valid mappings between them."""

import pytest
from geneweaver.core.enum import (
    AdminLevel,
    AdminLevelInt,
    CurationAssignment,
    CurationAssignmentInt,
    GeneIdentifier,
    GeneIdentifierInt,
    Microarray,
    MicroarrayInt,
    ScoreType,
    ScoreTypeInt,
    Species,
    SpeciesInt,
)


@pytest.mark.parametrize(
    ("enum_class", "int_enum_class"),
    [
        (CurationAssignment, CurationAssignmentInt),
        (ScoreType, ScoreTypeInt),
        (AdminLevel, AdminLevelInt),
        (Species, SpeciesInt),
        (GeneIdentifier, GeneIdentifierInt),
        (Microarray, MicroarrayInt),
    ],
)
def test_enum_int_mapping(enum_class, int_enum_class):
    """Test that Enum and IntEnum has valid mappings between them."""
    for enum in enum_class:
        assert str(int_enum_class[enum.name]) == str(enum)
        assert int(int_enum_class[enum.name]) == int(enum)
        assert int_enum_class[enum.name].as_str() == enum
        assert int_enum_class[enum.name] == enum.as_int()
        assert int_enum_class(enum.value).as_str() == enum
        assert int_enum_class(enum.value) == enum.as_int()

    for int_enum in int_enum_class:
        assert int(enum_class[int_enum.name]) == int(int_enum)
        assert str(enum_class[int_enum.name]) == str(int_enum)
        assert enum_class[int_enum.name].as_int() == int_enum
        assert enum_class[int_enum.name] == int_enum.as_str()
        assert enum_class(int_enum.value).as_int() == int_enum
        assert enum_class(int_enum.value) == int_enum.as_str()

    assert set(e.name for e in enum_class) == set(e.name for e in int_enum_class)
