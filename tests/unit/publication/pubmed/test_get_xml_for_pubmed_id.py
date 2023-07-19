"""Test the get_xml_for_pubmed_id function."""
from unittest.mock import Mock, patch
from xml.etree import ElementTree

import pytest
from geneweaver.core.exc import ExternalAPIError
from geneweaver.core.publication.pubmed import get_xml_for_pubmed_id

from tests.unit.publication.pubmed.const import EXAMPLE_PARTIAL_XML_RESPONSES
from tests.utils import abbreviate_string_param


@pytest.mark.parametrize(
    ("xml_response", "keys"), EXAMPLE_PARTIAL_XML_RESPONSES, ids=abbreviate_string_param
)
def test_get_xml_for_pubmed_id(xml_response, keys):
    """Test get_xml_for_pubmed_id with simple XML responses."""
    mock_response = Mock()
    mock_response.text = xml_response
    mock_response.ok = True

    expected = ElementTree.fromstring(xml_response.encode("utf-8"))

    # Patch requests.get to return the mock response.
    with patch("requests.get", return_value=mock_response) as mock_get:
        result = get_xml_for_pubmed_id("some_pubmed_id")

    for key in keys:
        result = result.find(key)
        expected = expected.find(key)

    r_text = result.text
    e_text = expected.text

    assert mock_get.called
    assert mock_get.call_count == 1
    assert r_text == e_text


def test_get_xml_for_pubmed_id_raises_external_api_error():
    """Test get_xml_for_pubmed_id raises ExternalAPIError."""
    mock_response = Mock()
    mock_response.ok = False

    # Patch requests.get to return the mock response.
    with patch("requests.get", return_value=mock_response) as mock_get:
        with pytest.raises(ExternalAPIError):
            get_xml_for_pubmed_id("some_pubmed_id")

    assert mock_get.called
    assert mock_get.call_count == 1


def test_get_xml_with_pubmed_like_examples(pubmed_xml_string):
    """Test get_xml_for_pubmed_id with example XML responses."""
    mock_response = Mock()
    mock_response.text = pubmed_xml_string
    mock_response.ok = True

    # Patch requests.get to return the mock response.
    with patch("requests.get", return_value=mock_response) as mock_get:
        result = get_xml_for_pubmed_id("some_pubmed_id")

    assert mock_get.called
    assert mock_get.call_count == 1
    assert result is not None
