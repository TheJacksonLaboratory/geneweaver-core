"""Utility functions for tests."""
from typing import Any


def abbreviate_string_param(param: Any) -> str:  # noqa: ANN401
    """Abbreviate a pytest parameter.

    Function to abbreviate a string or dict parameter for pytest parametrization. This
    will be used as the `ids` parameter for a pytest fixture. e.g.

    @pytest.fixture(params=[PUBMED_XML_01, PUBMED_XML_02], ids=abbreviate_string_param)

    Using this function prevents pytest from printing the entire string or dict in the
    test report, which can be very long and make it difficult to read.

    :param param: The test parameter
    :type param: Any

    :returns: The abbreviated string representation of the parameter if it's a string
    and longer than 10 characters, or a dict and has more than 5 items, otherwise it
    just returns the string representation of the parameter.
    """
    if isinstance(param, str) and len(param) > 15:
        return param[:15] + "..."
    elif isinstance(param, dict) and len(param) > 5:
        return str({k: v for k, v in list(param.items())[:5]}) + "..."
    else:
        return str(param)
