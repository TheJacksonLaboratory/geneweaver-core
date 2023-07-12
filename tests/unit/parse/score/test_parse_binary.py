"""Tests for the parse_binary function."""
# ruff: noqa: ANN001, ANN201
import pytest
from geneweaver.core.parse.score import (
    ScoreType,
    parse_binary,
)


@pytest.mark.parametrize(
    "input_string",
    [
        "binary",
        "ignore_this",
        "",
        "123",
        "1.0",
        "1.0.0",
        "bin" "\n",
        " ",
        "binary ",
        " binary",
        "\t",
    ],
)
def test_parse_binary(input_string):
    """Tests the parse_binary function."""
    result = parse_binary(input_string)
    assert result.score_type == ScoreType.BINARY
    assert result.threshold == 1
