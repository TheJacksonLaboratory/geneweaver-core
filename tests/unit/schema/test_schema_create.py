"""Test that we can create all of the schema objects from a dict."""
import pytest
from geneweaver.core.schema.gene import Gene, GeneValue
from geneweaver.core.schema.geneset import BatchUpload, Geneset, GenesetUpload
from geneweaver.core.schema.group import Group, UserAdminGroup
from geneweaver.core.schema.ontology import Ontology, OntologyDB
from geneweaver.core.schema.project import Project, ProjectCreate
from geneweaver.core.schema.publication import Publication
from geneweaver.core.schema.stubgenerator import StubGenerator
from geneweaver.core.schema.user import UserFull


@pytest.mark.xfail()
def test_gene_schema(gene_data: dict) -> None:
    """Test creating a gene from a dict."""
    gene = Gene(**gene_data)
    assert gene.id == gene_data["id"]
    assert gene.reference_id == gene_data["reference_id"]
    assert gene.gdb_id == gene_data["gdb_id"]
    assert gene.species_id == gene_data["species_id"]
    assert gene.preference == gene_data["preference"]
    assert gene.date == gene_data["date"]
    assert gene.old_ids == gene_data["old_ids"]


def test_gene_value_schema(gene_value_data: dict) -> None:
    """Test creating a gene value from a dict."""
    gene_value = GeneValue(**gene_value_data)
    assert gene_value.gene_id == gene_value_data["gene-id"]
    assert gene_value.value == gene_value_data["value"]


def test_geneset_schema(geneset_data: dict) -> None:
    """Test creating a geneset from a dict."""
    geneset = Geneset(**geneset_data)
    assert geneset.name == geneset_data["name"]
    assert geneset.abbreviation == geneset_data["abbreviation"]
    assert geneset.description == geneset_data["description"]
    assert geneset.count == geneset_data["count"]
    assert geneset.threshold_type == geneset_data["threshold_type"]
    assert geneset.threshold == geneset_data["threshold"]
    assert geneset.gene_id_type == geneset_data["gene_id_type"]
    assert str(geneset.created) == str(geneset_data["created"])
    assert geneset.admin_flag == geneset_data["admin_flag"]
    assert str(geneset.updated) == str(geneset_data["updated"])
    assert geneset.status == geneset_data["status"]
    assert geneset.gsv_qual == geneset_data["gsv_qual"]
    assert geneset.attribution == geneset_data["attribution"]
    assert geneset.is_edgelist == geneset_data["is_edgelist"]


def test_geneset_upload_schema(geneset_upload_data: dict) -> None:
    """Test creating a geneset upload from a dict."""
    geneset_upload = GenesetUpload(**geneset_upload_data)
    assert geneset_upload.name == geneset_upload_data["name"]
    assert geneset_upload.label == geneset_upload_data["label"]
    assert geneset_upload.score_type == geneset_upload_data["score-type"]
    assert geneset_upload.description == geneset_upload_data["description"]
    assert geneset_upload.pubmed_id == geneset_upload_data["pubmed-id"]
    assert geneset_upload.access == geneset_upload_data["access"]
    assert geneset_upload.groups == geneset_upload_data["groups"]
    assert geneset_upload.species == geneset_upload_data["species"]
    assert geneset_upload.gene_identifier == geneset_upload_data["gene-identifier"]
    assert len(geneset_upload.gene_list) == len(geneset_upload_data["gene-list"])


def test_batch_upload_schema(batch_upload_data: dict) -> None:
    """Test creating a batch upload from a dict."""
    batch_upload = BatchUpload(**batch_upload_data)
    assert batch_upload.batch_file == batch_upload_data["batch_file"]
    assert batch_upload.curation_group == batch_upload_data["curation_group"]


def test_group_schema(group_data: dict) -> None:
    """Test creating a group from a dict."""
    group = Group(**group_data)
    assert group.name == group_data["name"]
    assert group.id == group_data["id"]
    assert group.private == group_data["private"]
    assert str(group.created) == group_data["created"]
    assert group.stubgenerators == group_data["stubgenerators"]


def test_user_admin_group_schema(user_admin_group_data: dict) -> None:
    """Test creating a user admin group from a dict."""
    user_admin_group = UserAdminGroup(**user_admin_group_data)
    assert user_admin_group.name == user_admin_group_data["name"]
    assert user_admin_group.public == user_admin_group_data["public"]
    assert str(user_admin_group.created) == user_admin_group_data["created"]


def test_project_schema(project_data: dict) -> None:
    """Test creating a project from a dict."""
    project = Project(**project_data)
    assert project.id == project_data["id"]
    assert project.name == project_data["name"]
    assert project.groups == project_data["groups"]
    assert project.session_id == project_data["session_id"]
    assert project.created == project_data["created"]
    assert project.notes == project_data["notes"]
    assert project.star == project_data["star"]


def test_project_create_schema(project_create_data: dict) -> None:
    """Test creating a project create from a dict."""
    project_create = ProjectCreate(**project_create_data)
    assert project_create.name == project_create_data["name"]
    assert project_create.notes == project_create_data["notes"]


def test_publication_schema(publication_data: dict) -> None:
    """Test creating a publication from a dict."""
    publication = Publication(**publication_data)
    assert publication.id == publication_data["id"]
    assert publication.authors == publication_data["authors"]
    assert publication.title == publication_data["title"]
    assert publication.abstract == publication_data["abstract"]
    assert publication.journal == publication_data["journal"]
    assert publication.volume == publication_data["volume"]
    assert publication.pages == publication_data["pages"]
    assert publication.month == publication_data["month"]
    assert publication.year == publication_data["year"]
    assert publication.pages == publication_data["pages"]


def test_stubgenerator_schema(stub_generator_data: dict) -> None:
    """Test creating a stub generator from a dict."""
    stubgenerator = StubGenerator(**stub_generator_data)
    assert stubgenerator.name == stub_generator_data["name"]
    assert stubgenerator.id == stub_generator_data["id"]
    assert stubgenerator.querystring == stub_generator_data["querystring"]
    assert stubgenerator.last_update == stub_generator_data["last_update"]


def test_user_schema(user_data: dict) -> None:
    """Test creating a User from a dict."""
    user = UserFull(**user_data)
    assert user.id == user_data["id"]
    assert user.email == user_data["email"]
    assert user.first_name == user_data["first_name"]
    assert user.last_name == user_data["last_name"]
    assert user.email == user_data["email"]
    assert user.prefs == user_data["prefs"]
    assert user.admin == user_data["admin"]
    assert user.is_guest == user_data["is_guest"]
    assert user.groups == user_data["groups"]
    assert user.stubgenerators == user_data["stubgenerators"]


def test_ontology_schema(ontology_data: dict) -> None:
    """Test creating an ontology from a dict."""
    ontology = Ontology(**ontology_data)
    assert ontology.ontology_id == ontology_data["ontology_id"]
    assert ontology.reference_id == ontology_data["reference_id"]
    assert ontology.name == ontology_data["name"]
    assert ontology.description == ontology_data["description"]
    assert ontology.children == ontology_data["children"]
    assert ontology.parents == ontology_data["parents"]
    assert ontology.ontdb_id == ontology_data["ontdb_id"]
    assert ontology.ro_ont_id == ontology_data["ro_ont_id"]


def test_ontology_db_schema(ontology_db_data: dict) -> None:
    """Test creating an ontology db from a dict."""
    ontology_db = OntologyDB(**ontology_db_data)
    assert ontology_db.ontology_db_id == ontology_db_data["ontology_db_id"]
    assert ontology_db.name == ontology_db_data["name"]
    assert ontology_db.prefix == ontology_db_data["prefix"]
    assert ontology_db.ncbo_id == ontology_db_data["ncbo_id"]
    assert ontology_db.date == ontology_db_data["date"]
    assert ontology_db.linkout_url == ontology_db_data["linkout_url"]
    assert ontology_db.ncbo_vid == ontology_db_data["ncbo_vid"]
