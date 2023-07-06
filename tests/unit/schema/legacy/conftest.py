"""Fixtures for legacy schema tests."""
import pytest


@pytest.fixture()
def add_geneset_by_user_publication_data() -> dict:
    """Return a dict of data for AddGenesetByUserPublication."""
    return {
        "pub_abstract": "pub_abstract",
        "pub_authors": "pub_authors",
        "pub_journal": "pub_journal",
        "pub_pages": "pub_pages",
        "pub_pubmed": "pub_pubmed",
        "pub_title": "pub_title",
        "pub_volume": "pub_volume",
        "pub_year": "2019",
    }


@pytest.fixture()
def add_geneset_by_user_data() -> dict:
    """Return a dict of data for AddGenesetByUser."""
    return {
        "gene_identifier": "gene_identifier",
        "gs_abbreviation": "gs_abbreviation",
        "gs_description": "gs_description",
        "gs_name": "gs_name",
        "gs_threshold_type": 1,
        "permissions": "private",
        "publication": None,
        "select_groups": ["1"],
        "sp_id": "1",
        "file_text": "file_text",
    }


@pytest.fixture()
def add_geneset_by_user_file_data() -> dict:
    """Return a dict of data for AddGenesetByUserFile."""
    return {
        "gene_identifier": "gene_identifier",
        "gs_abbreviation": "gs_abbreviation",
        "gs_description": "gs_description",
        "gs_name": "gs_name",
        "gs_threshold_type": 1,
        "permissions": "private",
        "publication": None,
        "select_groups": ["1"],
        "sp_id": "1",
        "file_url": "https://example.com",
    }
