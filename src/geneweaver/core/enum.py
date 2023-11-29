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
    """Species enum to match Geneweaver database."""

    ALL = 0
    MUS_MUSCULUS = 1
    HOMO_SAPIENS = 2
    RATTUS_NORVEGICUS = 3
    DANIO_RERIO = 4
    DROSOPHILA_MELANOGASTER = 5
    MACACA_MULATTA = 6
    CAENORHABDITIS_ELEGANS = 8
    SACCHAROMYCES_CEREVISIAE = 9
    GALLUS_GALLUS = 10
    CANIS_FAMILIARIS = 11

    def __str__(self) -> str:
        """Render as a string."""
        return self.name


class GeneIdentifier(int, Enum):
    """Gene Identifier types to match Geneweaver database."""

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

    def __str__(self) -> str:
        """Render as a string."""
        return self.name


class Microarray(int, Enum):
    """Microarray types (does not match geneweaver database)."""

    AFFYMETRIX_C_ELEGANS_GENOME_ARRAY = 100
    AFFYMETRIX_DROSOPHILA_GENOME_2_0 = 101
    AFFYMETRIX_HT_HUMAN_GENOME_U133A = 102
    AFFYMETRIX_HUMAN_35K_SET = 103
    AFFYMETRIX_HUMAN_35K_SUBA = 104
    AFFYMETRIX_HUMAN_35K_SUBB = 105
    AFFYMETRIX_HUMAN_35K_SUBC = 106
    AFFYMETRIX_HUMAN_35K_SUBD = 107
    AFFYMETRIX_HUMAN_GENOME_U133A = 108
    AFFYMETRIX_HUMAN_GENOME_U133A_2_0 = 109
    AFFYMETRIX_HUMAN_GENOME_U133B = 110
    AFFYMETRIX_HUMAN_GENOME_U133_PLUS_2_0 = 111
    AFFYMETRIX_HUMAN_GENOME_U133_SET = 112
    AFFYMETRIX_HUMAN_HG_FOCUS_TARGET = 113
    AFFYMETRIX_MOUSE_EXON_1_0_ST = 114
    AFFYMETRIX_MOUSE_EXPRESSION_430A = 115
    AFFYMETRIX_MOUSE_EXPRESSION_430B = 116
    AFFYMETRIX_MOUSE_EXPRESSION_430_SET = 117
    AFFYMETRIX_MOUSE_GENE_1_0_ST_ARRAY = 118
    AFFYMETRIX_MOUSE_GENOME_430_2_0 = 119
    AFFYMETRIX_MOUSE_GENOME_430A_2_0 = 120
    AFFYMETRIX_MURINE_11K_SET = 121
    AFFYMETRIX_MURINE_11K_SUBA = 122
    AFFYMETRIX_MURINE_11K_SUBB = 123
    AFFYMETRIX_MURINE_GENOME_U74A = 124
    AFFYMETRIX_MURINE_GENOME_U74B = 125
    AFFYMETRIX_MURINE_GENOME_U74C = 126
    AFFYMETRIX_MURINE_GENOME_U74_SET = 127
    AFFYMETRIX_MURINE_GENOME_U74_VERSION_2 = 128
    AFFYMETRIX_MURINE_GENOME_U74_VERSION_2_SET = 129
    AFFYMETRIX_RAT_EXON_1_0_ST = 130
    AFFYMETRIX_RAT_EXPRESSION_230A = 131
    AFFYMETRIX_RAT_EXPRESSION_230B = 132
    AFFYMETRIX_RAT_EXPRESSION_230_SET = 133
    AFFYMETRIX_RAT_GENOME_230_2_0 = 134
    AFFYMETRIX_RHESUS_MACAQUE_GENOME = 135
    AFFYMETRIX_YEAST_GENOME_2_0_ARRAY = 136
    AFFYMETRIX_YEAST_GENOME_S98_ARRAY = 137
    AFFYMETRIX_ZEBRAFISH_GENOME = 138
    AGILENT_MOUSE_G4121A_TOXICOGENOMICS = 139
    AGILENT_MOUSE_WHOLE_GENOME_G4122F = 140
    ILLUMINA_HUMAN_6_V2_0 = 141
    ILLUMINA_MOUSEREF_8_V2_0 = 142
    ILLUMINA_MOUSEWG_6_V1_1 = 143
    ILLUMINA_MOUSEWG_6_V2_0 = 144

    def __str__(self) -> str:
        """Render as a string."""
        return self.name
