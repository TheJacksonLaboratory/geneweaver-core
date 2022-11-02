import pytest
from datetime import datetime


@pytest.fixture
def gene_data():
    return {
        'id': 1,
        'reference_id': '1',
        'gdb_id': 1,
        'species_id': 1,
        'preference': True,
        'date': '2019-01-01',
        'old_ids': [1]
    }


@pytest.fixture
def gene_value_data():
    return {
        'gene-id': '1',
        'value': '1'
    }


@pytest.fixture
def geneset_data():
    return {
        'name': 'name',
        'abbreviation': 'abbreviation',
        'description': 'description',
        'count': 1,
        'threshold_type': 1,
        'threshold': '1',
        'gene_id_type': 1,
        'created': '2019-01-01',
        'admin_flag': 'admin_flag',
        'updated': str(datetime.now()),
        'status': 'status',
        'gsv_qual': 'gsv_qual',
        'attribution': 1,
        'is_edgelist': True
    }


@pytest.fixture
def geneset_upload_data():
    return {
        'name': 'name',
        'label': 'label',
        'score-type': 1,
        'description': 'description',
        'pubmed-id': '1',
        'access': 'private',
        'groups': ['group'],
        'species': 'species',
        'gene-identifiers': 'gene_identifiers',
        'gene-list': [{
            'gene-id': '1',
            'value': '1'
        }]
    }


@pytest.fixture
def batch_upload_data():
    return {
        'batch_file': 'batch_file',
        'curation_group': ['group']
    }


@pytest.fixture
def group_data():
    return {
        'id': 1,
        'name': 'name',
        'private': True,
        'created': '2019-01-01',
        'stubgenerators': [],
    }


@pytest.fixture
def user_admin_group_data():
    return {
        'name': 'name',
        'public': True,
        'created': '2019-01-01'
    }


@pytest.fixture
def project_data():
    return {
        'id': 1,
        'name': 'name',
        'groups': ['1'],
        'session_id': 'session_id',
        'created': '2019-01-01',
        'notes': 'notes',
        'star': 't'
    }


@pytest.fixture
def project_create_data():
    return {
        'name': 'name',
        'notes': 'notes',
    }


@pytest.fixture
def publication_data():
    return {
        'id': 1,
        'authors': 'authors',
        'title': 'title',
        'abstract': 'abstract',
        'journal': 'journal',
        'volume': 'volume',
        'pages': 'pages',
        'month': 'month',
        'year': 1999,
        'pubmed': 23456
    }


@pytest.fixture
def stub_generator_data():
    return {
        'id': 1,
        'name': 'name',
        'querystring': 'querystring',
        'last_update': '2019-01-01',
    }


@pytest.fixture
def user_data():
    return {
        'id': 1,
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'prefs': 'prefs',
        'admin': 0,
        'is_guest': False,
        'groups': ['1'],
        'stubgenerators': [],
    }