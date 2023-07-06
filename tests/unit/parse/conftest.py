"""Fixture for the parse module."""
# ruff: noqa: ANN001
import pytest

from tests.unit.parse import const


@pytest.fixture(
    params=[
        const.EXAMPLE_BATCH_FILE,
        "\n".join(const.EXAMPLE_BATCH_FILE.splitlines()[:124]),
        "\r".join(const.EXAMPLE_BATCH_FILE.splitlines()[:124]),
        "\n".join(const.EXAMPLE_BATCH_FILE.splitlines()[:309]),
        "\r".join(const.EXAMPLE_BATCH_FILE.splitlines()[:309]),
    ]
)
def example_batch_file_contents(request) -> str:
    """Fixture for the contents of example batch files."""
    return request.param
