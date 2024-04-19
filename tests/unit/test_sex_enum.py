"""Test the enum.Sex enum."""

import pytest
from geneweaver.core.enum import Sex


def test_sex_enum_as_string():
    """Test that the Sex enum renders to string as expected."""

    assert str(Sex.FEMALE) == "Female"
    assert str(Sex.MALE) == "Male"
    assert str(Sex.BOTH) == "Both"


def test_initialize_sex_enum_from_string():
    """Test that we can initialize the Sex enum as expected."""

    assert Sex("Female") == Sex.FEMALE
    assert Sex("Male") == Sex.MALE
    assert Sex("Both") == Sex.BOTH


@pytest.mark.parametrize(
    "invalid_sex_value",
    [
        "test",
        "another",
        "CAPS",
        "MALE",
        "male",
        "FEMALE",
        "female",
        "BOTH",
        "both",
        "neither",
        "either",
        "none",
        "all",
        "unknown",
        "other",
        "12345",
        "1.2345",
        "0",
        "None",
    ],
)
def test_sex_enum_raises_error_when_initialized_with_invalid_value(invalid_sex_value):
    """Test that initializing the Sex enum with an invalid value raises an error."""

    with pytest.raises(ValueError) as error_info:
        Sex(invalid_sex_value)

    assert (
        str(error_info.value) == f"'{invalid_sex_value}' is not a valid Sex"
    )
