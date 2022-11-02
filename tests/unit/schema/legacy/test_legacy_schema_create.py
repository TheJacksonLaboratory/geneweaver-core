from jax.geneweaver.core.schema.legacy_api import AddGenesetByUserPublication
from jax.geneweaver.core.schema.legacy_api import AddGenesetByUser
from jax.geneweaver.core.schema.legacy_api import AddGenesetByUserFile


def test_add_gs_by_user_pub_schema(add_geneset_by_user_publication_data):
    """Test the AddGenesetByUserPublication class."""
    pub = AddGenesetByUserPublication(**add_geneset_by_user_publication_data)
    assert pub.pub_abstract == add_geneset_by_user_publication_data['pub_abstract']
    assert pub.pub_authors == add_geneset_by_user_publication_data['pub_authors']
    assert pub.pub_journal == add_geneset_by_user_publication_data['pub_journal']
    assert pub.pub_pages == add_geneset_by_user_publication_data['pub_pages']
    assert pub.pub_pubmed == add_geneset_by_user_publication_data['pub_pubmed']
    assert pub.pub_title == add_geneset_by_user_publication_data['pub_title']
    assert pub.pub_volume == add_geneset_by_user_publication_data['pub_volume']
    assert pub.pub_year == add_geneset_by_user_publication_data['pub_year']


def _shared_add_gs_by_user_asserts(inst, inst_dict):
    assert inst.gene_identifier == inst_dict['gene_identifier']
    assert inst.gs_abbreviation == inst_dict['gs_abbreviation']
    assert inst.gs_description == inst_dict['gs_description']
    assert inst.gs_name == inst_dict['gs_name']
    assert inst.gs_threshold_type == inst_dict['gs_threshold_type']
    assert inst.permissions == inst_dict['permissions']
    assert inst.publication == inst_dict['publication']
    assert inst.select_groups == inst_dict['select_groups']
    assert inst.sp_id == inst_dict['sp_id']


def test_add_gs_by_user_schema(add_geneset_by_user_data):
    """Test the AddGenesetByUser class."""
    gs = AddGenesetByUser(**add_geneset_by_user_data)
    _shared_add_gs_by_user_asserts(gs, add_geneset_by_user_data)
    assert gs.file_text == add_geneset_by_user_data['file_text']


def test_add_gs_by_user_file_schema(add_geneset_by_user_file_data):
    """Test the AddGenesetByUserFile class."""
    gs = AddGenesetByUserFile(**add_geneset_by_user_file_data)
    _shared_add_gs_by_user_asserts(gs, add_geneset_by_user_file_data)
    assert gs.file_url == add_geneset_by_user_file_data['file_url']
