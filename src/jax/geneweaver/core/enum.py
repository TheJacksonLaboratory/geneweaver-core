from enum import Enum


class CurationAssignment(int, Enum):
    UNASSIGNED = 1
    ASSIGNED = 2
    READY_FOR_REVIEW = 3
    REVIEWED = 4
    APPROVED = 5


class GenesetScoreTypeStr(str, Enum):
    P_VALUE = 'p-value'
    Q_VALUE = 'q-value'
    BINARY = 'binary'
    CORRELATION = 'correlation'
    EFFECT = 'effect'


class GenesetScoreType(int, Enum):
    P_VALUE = 1
    Q_VALUE = 2
    BINARY = 3
    CORRELATION = 4
    EFFECT = 5


class GenesetAccess(str, Enum):
    PRIVATE = 'private'
    PUBLIC = 'public'
