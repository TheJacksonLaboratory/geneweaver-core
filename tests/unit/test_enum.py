
from geneweaver.core.enum import CurationAssignment
from geneweaver.core.enum import GenesetAccess
from geneweaver.core.enum import GenesetScoreType
from geneweaver.core.enum import GenesetScoreTypeStr


def test_curation_assignment():
    """Test the CurationAssignment enum."""
    assert CurationAssignment.UNASSIGNED == 1
    assert CurationAssignment.ASSIGNED == 2
    assert CurationAssignment.READY_FOR_REVIEW == 3
    assert CurationAssignment.REVIEWED == 4
    assert CurationAssignment.APPROVED == 5


def test_curation_assignment_from_int():
    """Test the CurationAssignment enum creation from an int."""
    assert CurationAssignment(1) == CurationAssignment.UNASSIGNED
    assert CurationAssignment(2) == CurationAssignment.ASSIGNED
    assert CurationAssignment(3) == CurationAssignment.READY_FOR_REVIEW
    assert CurationAssignment(4) == CurationAssignment.REVIEWED
    assert CurationAssignment(5) == CurationAssignment.APPROVED


def test_geneset_access():
    """Test the GenesetAccess enum."""
    assert GenesetAccess.PRIVATE == 'private'
    assert GenesetAccess.PUBLIC == 'public'


def test_geneset_access_from_string():
    """Test the GenesetAccess enum creation from a string."""
    assert GenesetAccess('private') == GenesetAccess.PRIVATE
    assert GenesetAccess('public') == GenesetAccess.PUBLIC


def test_geneset_score_type():
    """Test the GenesetScoreType enum."""
    assert GenesetScoreType.P_VALUE == 1
    assert GenesetScoreType.Q_VALUE == 2
    assert GenesetScoreType.BINARY == 3
    assert GenesetScoreType.CORRELATION == 4
    assert GenesetScoreType.EFFECT == 5


def test_geneset_score_type_from_int():
    """Test the GenesetScoreType enum creation from an int."""
    assert GenesetScoreType(1) == GenesetScoreType.P_VALUE
    assert GenesetScoreType(2) == GenesetScoreType.Q_VALUE
    assert GenesetScoreType(3) == GenesetScoreType.BINARY
    assert GenesetScoreType(4) == GenesetScoreType.CORRELATION
    assert GenesetScoreType(5) == GenesetScoreType.EFFECT


def test_geneset_score_type_str():
    """Test the GenesetScoreTypeStr enum."""
    assert GenesetScoreTypeStr.P_VALUE == 'p-value'
    assert GenesetScoreTypeStr.Q_VALUE == 'q-value'
    assert GenesetScoreTypeStr.BINARY == 'binary'
    assert GenesetScoreTypeStr.CORRELATION == 'correlation'
    assert GenesetScoreTypeStr.EFFECT == 'effect'


def test_geneset_score_type_str_from_string():
    """Test the GenesetScoreTypeStr enum creation from a string."""
    assert GenesetScoreTypeStr('p-value') == GenesetScoreTypeStr.P_VALUE
    assert GenesetScoreTypeStr('q-value') == GenesetScoreTypeStr.Q_VALUE
    assert GenesetScoreTypeStr('binary') == GenesetScoreTypeStr.BINARY
    assert GenesetScoreTypeStr('correlation') == GenesetScoreTypeStr.CORRELATION
    assert GenesetScoreTypeStr('effect') == GenesetScoreTypeStr.EFFECT

