"""Fixtures for the pubmed api services."""
from xml.etree import ElementTree

import pytest

from tests.unit.publication.pubmed.const import (
    PUBMED_XML_01,
    PUBMED_XML_02,
)
from tests.utils import abbreviate_string_param


@pytest.fixture(params=[PUBMED_XML_01, PUBMED_XML_02], ids=abbreviate_string_param)
def pubmed_xml_string(request):
    """Fixture wrap for pubmed xml strings."""
    return request.param


@pytest.fixture()
def pubmed_xml(pubmed_xml_string):
    """Load the pubmed xml string into xml element tree."""
    return ElementTree.fromstring(pubmed_xml_string)
