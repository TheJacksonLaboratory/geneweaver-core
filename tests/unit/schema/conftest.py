"""Unit test fixtures for the schema module."""
from datetime import datetime

import pytest


@pytest.fixture()
def gene_data() -> dict:
    """Provide example gene data."""
    return {
        "id": 1,
        "reference_id": "1",
        "gdb_id": 1,
        "species_id": 1,
        "preference": True,
        "date": "2019-01-01",
        "old_ids": [1],
    }


@pytest.fixture()
def gene_value_data() -> dict:
    """Provide example gene value data."""
    return {"gene-id": "1", "value": "1"}


@pytest.fixture()
def geneset_data() -> dict:
    """Provide example geneset data."""
    return {
        "name": "name",
        "abbreviation": "abbreviation",
        "description": "description",
        "count": 1,
        "threshold_type": 1,
        "threshold": "1",
        "gene_id_type": 1,
        "created": "2019-01-01",
        "admin_flag": "admin_flag",
        "updated": str(datetime.now()),
        "status": "status",
        "gsv_qual": "gsv_qual",
        "attribution": 1,
        "is_edgelist": True,
    }


@pytest.fixture()
def geneset_upload_data() -> dict:
    """Provide example geneset upload data."""
    return {
        "name": "name",
        "label": "label",
        "score-type": 1,
        "description": "description",
        "pubmed-id": "1",
        "access": "private",
        "groups": ["group"],
        "species": "species",
        "gene-identifier": "gene_identifier",
        "gene-list": [{"gene-id": "1", "value": "1"}],
    }


@pytest.fixture()
def batch_upload_data() -> dict:
    """Provide example batch upload data."""
    return {"batch_file": "batch_file", "curation_group": ["group"]}


@pytest.fixture()
def group_data() -> dict:
    """Provide example group data."""
    return {
        "id": 1,
        "name": "name",
        "private": True,
        "created": "2019-01-01",
        "stubgenerators": [],
    }


@pytest.fixture()
def user_admin_group_data() -> dict:
    """Provide example user admin group data."""
    return {"name": "name", "public": True, "created": "2019-01-01"}


@pytest.fixture()
def project_data() -> dict:
    """Provide example project data."""
    return {
        "id": 1,
        "name": "name",
        "groups": ["1"],
        "session_id": "session_id",
        "created": "2019-01-01",
        "notes": "notes",
        "star": "t",
    }


@pytest.fixture()
def project_create_data() -> dict:
    """Provide example project create data."""
    return {
        "name": "name",
        "notes": "notes",
    }


@pytest.fixture()
def publication_data() -> dict:
    """Provide example publication data."""
    return {
        "id": 1,
        "authors": "authors",
        "title": "title",
        "abstract": "abstract",
        "journal": "journal",
        "volume": "volume",
        "pages": "pages",
        "month": "month",
        "year": 1999,
        "pubmed_id": 23456,
    }


@pytest.fixture()
def stub_generator_data() -> dict:
    """Provide example stub generator data."""
    return {
        "id": 1,
        "name": "name",
        "querystring": "querystring",
        "last_update": "2019-01-01",
    }


@pytest.fixture()
def user_data() -> dict:
    """Provide example user data."""
    return {
        "id": 1,
        "first_name": "first_name",
        "last_name": "last_name",
        "email": "email",
        "prefs": "prefs",
        "admin": 0,
        "is_guest": False,
        "groups": ["1"],
        "stubgenerators": [],
    }


@pytest.fixture()
def ontology_data() -> dict:
    """Provide example ontology data."""
    return {
        "ontology_id": 1,
        "reference_id": 1,
        "name": "name",
        "description": "description",
        "children": [],
        "parents": [],
        "ontdb_id": 1,
        "ro_ont_id": 1,
    }


@pytest.fixture()
def ontology_db_data() -> dict:
    """Provide example ontology db data."""
    return {
        "ontology_db_id": 1,
        "name": "name",
        "prefix": "prefix",
        "ncbo_id": "ncbo_id",
        "date": "2019-01-01",
        "linkout_url": "linkout_url",
        "ncbo_vid": "ncbo_vid",
    }
