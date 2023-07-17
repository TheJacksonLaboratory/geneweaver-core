"""Test the `authors_are_complete` function."""
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import authors_are_complete

from tests.unit.publication.pubmed.const import EXAMPLE_AUTHORS_LIST

CONSIDERED_COMPLETE = ["CompleteYN='N'" not in item for item in EXAMPLE_AUTHORS_LIST]


@pytest.mark.parametrize(
    ("xml_string", "expected_result"),
    zip(EXAMPLE_AUTHORS_LIST, CONSIDERED_COMPLETE),  # noqa: B905
)
def test_authors_are_complete(xml_string: str, expected_result: bool):
    """Tests for authors_are_complete function.

    :param xml_string: XML string to parse for the author list node
    :param expected_result: expected output of the function
    """
    author_list_node = ElementTree.fromstring(xml_string)
    assert authors_are_complete(author_list_node) == expected_result
