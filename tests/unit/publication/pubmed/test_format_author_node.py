"""Test the format_author_node function."""
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import format_author_node

from tests.unit.publication.pubmed.const import EXAMPLE_AUTHORS


@pytest.mark.parametrize(("xml_string", "expected_result"), EXAMPLE_AUTHORS)
def test_format_author_node(xml_string: str, expected_result: str):
    """Tests for format_author_node function.

    :param xml_string: XML string to parse for the author node
    :param expected_result: expected output of the function
    """
    author_node = ElementTree.fromstring(xml_string)
    assert format_author_node(author_node) == expected_result
