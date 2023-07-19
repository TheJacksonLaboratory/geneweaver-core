"""Test the extract date function."""
from xml.etree import ElementTree

import pytest
from geneweaver.core.publication.pubmed import extract_date

# Parameterized inputs and expected outputs
EXAMPLE_XML_DATES = [
    (
        "<root><PubDate><Year>2023</Year><Month>07"
        "</Month><Day>13</Day></PubDate></root>",
        {"year": "2023", "month": "07", "day": "13"},
    ),
    (
        "<root><PubDate><Year>2022</Year><Month>06"
        "</Month><Day>12</Day></PubDate></root>",
        {"year": "2022", "month": "06", "day": "12"},
    ),
    (
        "<root><PubDate><Year>2021</Year><Month>05"
        "</Month><Day>11</Day></PubDate></root>",
        {"year": "2021", "month": "05", "day": "11"},
    ),
    (
        "<root><PubDate><Year>2020</Year><Month>04"
        "</Month><Day>10</Day></PubDate></root>",
        {"year": "2020", "month": "04", "day": "10"},
    ),
    (
        "<root><PubDate><Year>2019</Year><Month>03"
        "</Month><Day>09</Day></PubDate></root>",
        {"year": "2019", "month": "03", "day": "09"},
    ),
    (
        "<root><PubDate><Year>2023</Year><Month>07</Month></PubDate></root>",
        {"year": "2023", "month": "07"},
    ),
    (
        "<root><PubDate><Year>2022</Year><Month>06</Month></PubDate></root>",
        {"year": "2022", "month": "06"},
    ),
    (
        "<root><PubDate><Year>2021</Year><Month>05</Month></PubDate></root>",
        {"year": "2021", "month": "05"},
    ),
    (
        "<root><PubDate><Year>2020</Year><Month>04</Month></PubDate></root>",
        {"year": "2020", "month": "04"},
    ),
    (
        "<root><PubDate><Year>2019</Year><Month>03</Month></PubDate></root>",
        {"year": "2019", "month": "03"},
    ),
    ("<root><PubDate><Year>2023</Year></PubDate></root>", {"year": "2023"}),
    ("<root><PubDate><Year>2022</Year></PubDate></root>", {"year": "2022"}),
    ("<root><PubDate><Year>2021</Year></PubDate></root>", {"year": "2021"}),
    ("<root><PubDate><Year>2020</Year></PubDate></root>", {"year": "2020"}),
    ("<root><PubDate><Year>2019</Year></PubDate></root>", {"year": "2019"}),
    ("<root></root>", {}),
    (
        "<root><PubDate><Month>07</Month><Day>13</Day></PubDate></root>",
        {"month": "07", "day": "13"},
    ),
    (
        "<root><PubDate><Month>06</Month><Day>12</Day></PubDate></root>",
        {"month": "06", "day": "12"},
    ),
    (
        "<root><PubDate><Month>05</Month><Day>11</Day></PubDate></root>",
        {"month": "05", "day": "11"},
    ),
    (
        "<root><PubDate><Month>04</Month><Day>10</Day></PubDate></root>",
        {"month": "04", "day": "10"},
    ),
]


@pytest.mark.parametrize(("xml_string", "expected_output"), EXAMPLE_XML_DATES)
def test_extract_date(xml_string, expected_output):
    """Test the extract date function."""
    # Parse the string to an XML element
    publication_xml = ElementTree.fromstring(xml_string)

    # Call the function with the XML element
    result = extract_date(publication_xml)

    # Assert that the function's output matches the expected output
    assert result == expected_output
