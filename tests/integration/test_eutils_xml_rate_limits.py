"""Test that the Eutils API rate limits don't break our usage."""
import pytest
from geneweaver.core.publication.pubmed import PUBMED_SVC_URL, get_xml_for_pubmed_id
from requests import get

from tests.integration.utils import call_function

N_RATE_TEST_ARGS = [
    (1, 1),
    (2, 1),
    (3, 1),
    (5, 1),
    (5, 3),
    (8, 3),
    (13, 3),
    (5, 5),
    (8, 10),
    (13, 10),
    (21, 10),
    (20, 20),
]


@pytest.mark.parametrize(("num_times", "rate"), N_RATE_TEST_ARGS)
def test_rate_for_eutils_publication_endpoint(num_times, rate):
    """Test rate for eutils API endpoint used by get_xml_for_pubmed_id."""
    url = PUBMED_SVC_URL.format("3981386")
    results = call_function(get, num_times, rate, url)
    for response in results:
        assert response.ok, response.text


@pytest.mark.parametrize(("num_times", "rate"), N_RATE_TEST_ARGS)
def test_rate_for_get_xml_for_pubmed_id(num_times, rate):
    """Test rate for get_xml_for_pubmed_id."""
    results = call_function(get_xml_for_pubmed_id, num_times, rate, "3981386")
    for response in results:
        assert response is not None, response
