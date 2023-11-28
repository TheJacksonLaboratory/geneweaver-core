"""Enum classes for the GeneWeaver project."""
from enum import Enum


class CurationAssignment(int, Enum):
    """Enum for the different types of curation assignments."""

    UNASSIGNED = 1
    ASSIGNED = 2
    READY_FOR_REVIEW = 3
    REVIEWED = 4
    APPROVED = 5


class GenesetScoreTypeStr(str, Enum):
    """Enum for the different types of geneset scores."""

    P_VALUE = "p-value"
    Q_VALUE = "q-value"
    BINARY = "binary"
    CORRELATION = "correlation"
    EFFECT = "effect"


class ScoreType(int, Enum):
    """Integer based Enum for the different types of geneset scores."""

    P_VALUE = 1
    Q_VALUE = 2
    BINARY = 3
    CORRELATION = 4
    EFFECT = 5


class GenesetAccess(str, Enum):
    """Enum for the different types of geneset access."""

    PRIVATE = "private"
    PUBLIC = "public"


class AnnotationType(str, Enum):
    """Enum for the different types of annotations."""

    MONARCH = "monarch"
    NCBO = "ncbo"


class AdminLevel(int, Enum):
    """Enum for the different levels of admin access."""

    NORMAL_USER = 0
    CURATOR = 1
    ADMIN = 2
    ADMIN_WITH_DEBUG = 3


class Species(int, Enum):
    ALL = 0
    MUSS_MUSCULUS = 1
    HOMO_SAPIENS = 2
    RATTUS_NORVEGICUS = 3
    DANIO_RERIO = 4
    DROSOPHILA_MELANOGASTER = 5
    MACACA_MULATTA = 6
    CAENORHABDITIS_ELEGANS = 8
    SACCHAROMYCES_CEREVISIAE = 9
    GALLUS_GALLUS = 10
    CANIS_FAMILIARIS = 11


class GeneIdentifier(int, Enum):
    ENTREZ = 1
    ENSEMBLE_GENE = 2
    ENSEMBLE_PROTEIN = 3
    ENSEMBLE_TRANSCRIPT = 4
    UNIGENE = 5
    GENE_SYMBOL = 7
    UNANNOTATED = 8
    MGI = 10
    HGNC = 11
    RGD = 12
    ZFIN = 13
    FLYBASE = 14
    WORMBASE = 15
    SGD = 16
    MIRBASE = 17
    CGNC = 20
