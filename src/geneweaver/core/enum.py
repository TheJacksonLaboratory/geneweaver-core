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


class GenesetScoreType(int, Enum):
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
