"""Test the get_publication function."""
from unittest.mock import patch
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import get_publication
from geneweaver.core.schema.publication import PublicationInfo

PUBMED_IDS = ["123456", "789012", "345678", "901234"]
EXAMPLE_XMLS = ["<root></root>", "<root></root>", "<root></root>", "<root></root>"]
EXAMPLE_PUBLICATION_FIELDS = [
    {
        "title": "Title1",
        "year": 2022,
        "authors": "John Doe",
        "abstract": "Abstract1",
        "journal": "Journal1",
        "volume": "Volume1",
        "pages": "Pages1",
        "month": "January",
        "pubmed_id": 123456,
    },
    {
        "title": "Title2",
        "year": 2023,
        "authors": "Jane Doe",
        "abstract": "Abstract2",
        "journal": "Journal2",
        "volume": "Volume2",
        "pages": "Pages2",
        "month": "February",
        "pubmed_id": 789012,
    },
    {
        "title": "Title3",
        "year": 2024,
        "authors": "John Smith",
        "abstract": "Abstract3",
        "journal": "Journal3",
        "volume": "Volume3",
        "pages": "Pages3",
        "month": "March",
        "pubmed_id": 345678,
    },
    {
        "title": "Title4",
        "year": 2025,
        "authors": "Jane Smith",
        "abstract": "Abstract4",
        "journal": "Journal4",
        "volume": "Volume4",
        "pages": "Pages4",
        "month": "April",
        "pubmed_id": 901234,
    },
]
EXAMPLE_PUBLICATION_INFOS = [
    PublicationInfo(
        title="Title1",
        year=2022,
        authors="John Doe",
        abstract="Abstract1",
        journal="Journal1",
        volume="Volume1",
        pages="Pages1",
        month="January",
        pubmed_id=123456,
    ),
    PublicationInfo(
        title="Title2",
        year=2023,
        authors="Jane Doe",
        abstract="Abstract2",
        journal="Journal2",
        volume="Volume2",
        pages="Pages2",
        month="February",
        pubmed_id=789012,
    ),
    PublicationInfo(
        title="Title3",
        year=2024,
        authors="John Smith",
        abstract="Abstract3",
        journal="Journal3",
        volume="Volume3",
        pages="Pages3",
        month="March",
        pubmed_id=345678,
    ),
    PublicationInfo(
        title="Title4",
        year=2025,
        authors="Jane Smith",
        abstract="Abstract4",
        journal="Journal4",
        volume="Volume4",
        pages="Pages4",
        month="April",
        pubmed_id=901234,
    ),
]


@patch("geneweaver.core.publication.pubmed.get_xml_for_pubmed_id")
@patch("geneweaver.core.publication.pubmed.extract_fields")
@pytest.mark.parametrize(
    ("pubmed_id", "xml_string", "publication_fields", "expected"),
    zip(  # noqa: B905
        PUBMED_IDS,
        EXAMPLE_XMLS,
        EXAMPLE_PUBLICATION_FIELDS,
        EXAMPLE_PUBLICATION_INFOS,
    ),
)
def test_get_publication(
    mock_extract_fields,
    mock_get_xml_for_pubmed_id,
    pubmed_id,
    xml_string,
    publication_fields,
    expected,
):
    """Test get_publication function using patched internal functions."""
    mock_get_xml_for_pubmed_id.return_value = ElementTree.fromstring(xml_string)
    mock_extract_fields.return_value = publication_fields

    result = get_publication(pubmed_id)

    assert result.dict() == expected.dict()

    mock_get_xml_for_pubmed_id.assert_called_once_with(pubmed_id)
    mock_extract_fields.assert_called_once()
