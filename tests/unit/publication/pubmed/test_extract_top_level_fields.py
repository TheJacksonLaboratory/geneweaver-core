"""Test extract_top_level_fields function."""
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import extract_top_level_fields

from tests.utils import abbreviate_string_param

EXAMPLE_XML_TOP_LEVEL_FIELDS = [
    (
        "<root>"
        "<ArticleTitle>Title1</ArticleTitle>"
        "<AbstractText>Abstract1</AbstractText>"
        "<Journal><Title>Journal1</Title></Journal>"
        "<Volume>Vol1</Volume>"
        "<MedlinePgn>Pgn1</MedlinePgn>"
        "</root>",
        {
            "title": "Title1",
            "abstract": "Abstract1",
            "journal": "Journal1",
            "volume": "Vol1",
            "pages": "Pgn1",
        },
    ),
    (
        "<root>"
        "<ArticleTitle>Title2</ArticleTitle>"
        "<AbstractText>Abstract2</AbstractText>"
        "<Journal><Title>Journal2</Title></Journal>"
        "<Volume>Vol2</Volume>"
        "<MedlinePgn>Pgn2</MedlinePgn>"
        "</root>",
        {
            "title": "Title2",
            "abstract": "Abstract2",
            "journal": "Journal2",
            "volume": "Vol2",
            "pages": "Pgn2",
        },
    ),
    (
        "<root>"
        "<ArticleTitle>Title3</ArticleTitle>"
        "<AbstractText>Abstract3</AbstractText>"
        "<Journal><Title></Title></Journal>"
        "<Volume></Volume>"
        "<MedlinePgn>Pgn3</MedlinePgn>"
        "</root>",
        {
            "title": "Title3",
            "abstract": "Abstract3",
            "journal": "",
            "volume": "",
            "pages": "Pgn3",
        },
    ),
    (
        "<root>"
        "<ArticleTitle>Title3</ArticleTitle>"
        "<AbstractText>Abstract3</AbstractText>"
        "<MedlinePgn>Pgn3</MedlinePgn>"
        "</root>",
        {"title": "Title3", "abstract": "Abstract3", "pages": "Pgn3"},
    ),
    (
        "<root>"
        "<ArticleTitle></ArticleTitle>"
        "<AbstractText></AbstractText>"
        "<Journal><Title>Journal4</Title></Journal>"
        "<Volume>Vol4</Volume>"
        "<MedlinePgn>Pgn4</MedlinePgn>"
        "</root>",
        {
            "title": "",
            "abstract": "",
            "journal": "Journal4",
            "volume": "Vol4",
            "pages": "Pgn4",
        },
    ),
    (
        "<root>"
        "<Journal><Title>Journal4</Title></Journal>"
        "<Volume>Vol4</Volume>"
        "<MedlinePgn>Pgn4</MedlinePgn>"
        "</root>",
        {"journal": "Journal4", "volume": "Vol4", "pages": "Pgn4"},
    ),
    ("<root></root>", {}),
]


@pytest.mark.parametrize(
    ("xml_string", "expected"),
    EXAMPLE_XML_TOP_LEVEL_FIELDS,
    ids=abbreviate_string_param,
)
def test_extract_top_level_fields(xml_string, expected):
    """Test that extract_top_level_fields returns the expected fields.

    No patching here!
    """
    publication_xml = ElementTree.fromstring(xml_string)
    assert extract_top_level_fields(publication_xml) == expected
