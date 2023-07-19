"""Test the extract_fields function."""
from unittest.mock import patch
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import extract_fields

from tests.unit.publication.pubmed.const import (
    EXAMPLE_FULL_XMLS,
    EXAMPLE_FULL_XMLS_EXPECTED,
)
from tests.utils import abbreviate_string_param


@patch("geneweaver.core.publication.pubmed.extract_top_level_fields")
@patch("geneweaver.core.publication.pubmed.extract_date")
@patch("geneweaver.core.publication.pubmed.extract_authors")
@pytest.mark.parametrize(
    ("xml_string", "expected"),
    zip(EXAMPLE_FULL_XMLS, EXAMPLE_FULL_XMLS_EXPECTED),  # noqa: B905
    ids=abbreviate_string_param,
)
def test_extract_fields_example(
    mock_extract_authors,
    mock_extract_date,
    mock_extract_top_level_fields,
    xml_string,
    expected,
):
    """Test extract_fields function with patching and with example XML."""
    mock_extract_top_level_fields.return_value = {
        k: v
        for k, v in expected.items()
        if k in ["title", "abstract", "journal", "volume", "pages"]
    }
    mock_extract_date.return_value = {
        k: v for k, v in expected.items() if k in ["year", "month", "day"]
    }
    mock_extract_authors.return_value = {
        k: v for k, v in expected.items() if k == "authors"
    }

    publication_xml = ElementTree.fromstring(xml_string)
    assert extract_fields(publication_xml) == expected

    mock_extract_top_level_fields.assert_called_once_with(publication_xml)
    mock_extract_date.assert_called_once_with(publication_xml)
    mock_extract_authors.assert_called_once_with(publication_xml)


def test_extract_fields_pubmed(pubmed_xml):
    """Test extract_fields function without patching and with PubMed-like XML."""
    result = extract_fields(pubmed_xml)
    assert result is not None
    assert type(result) == dict
    for item in ["title", "abstract", "journal", "volume", "pages"]:
        assert item in result.keys()
