"""Tests the extract_authors function."""
from unittest import mock
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import extract_authors

from tests.utils import abbreviate_string_param

MODULE = "geneweaver.core.publication.pubmed"

# Parameterized inputs and expected outputs
EXAMPLE_XML_AUTHORS = [
    (
        "<root><AuthorList CompleteYN='Y'><Author>"
        "<ForeName>John</ForeName><LastName>Doe</LastName>"
        "</Author></AuthorList></root>",
        {"authors": ["John Doe"]},
    ),
    (
        "<root><AuthorList CompleteYN='N'><Author>"
        "<ForeName>John</ForeName><LastName>Doe</LastName>"
        "</Author></AuthorList></root>",
        {"authors": ["John Doe", "et al."]},
    ),
    ("<root></root>", {}),
    (
        "<root><AuthorList CompleteYN='Y'><Author>"
        "<ForeName>John</ForeName><LastName>Doe</LastName>"
        "</Author><Author>"
        "<ForeName>Jane</ForeName><LastName>Doe</LastName>"
        "</Author></AuthorList></root>",
        {"authors": ["John Doe", "Jane Doe"]},
    ),
]


@pytest.mark.parametrize(
    ("xml_string", "expected_output"), EXAMPLE_XML_AUTHORS, ids=abbreviate_string_param
)
def test_extract_authors_mocked(xml_string, expected_output):
    """Test extract authors function with mocked internal functions."""
    # Parse the string to an XML element
    publication_xml = ElementTree.fromstring(xml_string)

    # Mock the internal function calls
    with mock.patch(
        f"{MODULE}.format_author_node",
        side_effect=lambda node: f"{node.findtext('ForeName')} "
        f"{node.findtext('LastName')}",
    ), mock.patch(
        f"{MODULE}.authors_are_complete",
        side_effect=lambda node: node.attrib["CompleteYN"] == "Y",
    ), mock.patch(
        f"{MODULE}.add_to_dict_if_not_none",
        side_effect=lambda d, k, v: v and d.update({k: v}),
    ):
        # Call the function with the XML element
        result = extract_authors(publication_xml)

        # Assert that the function's output matches the expected output
        assert result == expected_output


@pytest.mark.parametrize(
    ("xml_string", "expected_output"), EXAMPLE_XML_AUTHORS, ids=abbreviate_string_param
)
def test_extract_authors(xml_string, expected_output):
    """Test extract authors function without mocked internal functions."""
    # Parse the string to an XML element
    publication_xml = ElementTree.fromstring(xml_string)

    # Call the function with the XML element
    result = extract_authors(publication_xml)

    # Assert that the function's output matches the expected output
    assert result == expected_output
