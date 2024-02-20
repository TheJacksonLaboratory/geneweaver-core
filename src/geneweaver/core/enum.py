"""Enum classes for the GeneWeaver project."""

from enum import Enum, IntEnum
from typing import Union


class _StrToIntMixin:
    """Mixin for string based enums that have an integer representation."""

    @classmethod
    def _missing_(cls: Enum, key: Union[str, int]) -> Enum:
        """Return the key if it is not found."""
        try:
            key = int(key)
            return cls._int_class()(key).as_str()
        except ValueError:
            pass

    def __str__(self) -> str:
        """Render as a string."""
        return self.value

    def __int__(self) -> int:
        """Render as an integer."""
        return int(self._int_class()[self.name])

    def as_int(self) -> IntEnum:
        """Return the IntEnum version of this enum."""
        return self._int_class()[self.name]


class _IntToStrMixin:
    """Mixin for integer based enums that have a string representation."""

    @classmethod
    def _missing_(cls: IntEnum, key: Union[str, int]) -> IntEnum:
        """Return the key if it is not found."""
        if isinstance(key, str):
            return cls._str_class()(key).as_int()

    def __str__(self) -> str:
        """Render as a string."""
        return str(self._str_class()[self.name])

    def as_str(self) -> Enum:
        """Return the Enum (str) version of this enum."""
        return self._str_class()[self.name]


class GenesetTier(_StrToIntMixin, Enum):
    """Enum for the different types of geneset tiers."""

    TIER1 = "Tier I"
    TIER2 = "Tier II"
    TIER3 = "Tier III"
    TIER4 = "Tier IV"
    TIER5 = "Tier V"

    @staticmethod
    def _int_class() -> Enum:
        return GenesetTierInt


class GenesetTierInt(_IntToStrMixin, IntEnum):
    """Enum for the different types of geneset tiers."""

    TIER1 = 1
    TIER2 = 2
    TIER3 = 3
    TIER4 = 4
    TIER5 = 5

    @staticmethod
    def _str_class() -> Enum:
        return GenesetTier


class GenesetStatus(Enum):
    """Enum for the different types of geneset statuses."""

    NORMAL = "normal"
    DELETED = "deleted"
    PROVISIONAL = "provisional"
    DELAYED = "delayed"
    DELATED_PROCESSING = "delayed:processing"
    DEPRECATED = "deprecated"

    @classmethod
    def _missing_(cls: Enum, key: Union[str, int]) -> Enum:
        """Return the key if it is not found."""
        try:
            key = str(key).lower()
            for member in cls:
                if member.value == key:
                    return member
            split_key = key.split(":")[0]
            for member in cls:
                if member.value == split_key:
                    return member
        except ValueError:
            pass


class CurationAssignment(_StrToIntMixin, Enum):
    """Enum for the different types of curation assignments."""

    UNASSIGNED = "Unassigned"
    ASSIGNED = "Assigned"
    READY_FOR_REVIEW = "Ready for Review"
    REVIEWED = "Reviewed"
    APPROVED = "Approved"

    @staticmethod
    def _int_class() -> Enum:
        return CurationAssignmentInt


class CurationAssignmentInt(_IntToStrMixin, IntEnum):
    """Enum for the different types of curation assignments."""

    UNASSIGNED = 1
    ASSIGNED = 2
    READY_FOR_REVIEW = 3
    REVIEWED = 4
    APPROVED = 5

    @staticmethod
    def _str_class() -> Enum:
        return CurationAssignment


class ScoreType(_StrToIntMixin, Enum):
    """Enum for the different types of geneset scores."""

    P_VALUE = "p-value"
    Q_VALUE = "q-value"
    BINARY = "binary"
    CORRELATION = "correlation"
    EFFECT = "effect"

    @staticmethod
    def _int_class() -> Enum:
        return ScoreTypeInt


class ScoreTypeInt(_IntToStrMixin, IntEnum):
    """Integer based Enum for the different types of geneset scores."""

    P_VALUE = 1
    Q_VALUE = 2
    BINARY = 3
    CORRELATION = 4
    EFFECT = 5

    @staticmethod
    def _str_class() -> Enum:
        return ScoreType


class GenesetAccess(str, Enum):
    """Enum for the different types of geneset access."""

    PRIVATE = "private"
    PUBLIC = "public"


class Annotator(str, Enum):
    """Enum for the different types of annotations."""

    MONARCH = "monarch"
    NCBO = "ncbo"


class AdminLevel(_StrToIntMixin, Enum):
    """Enum for the different levels of admin access."""

    NORMAL_USER = "Normal User"
    CURATOR = "Curator"
    ADMIN = "Admin"
    ADMIN_WITH_DEBUG = "Admin with Debug"

    @staticmethod
    def _int_class() -> Enum:
        return AdminLevelInt


class AdminLevelInt(_IntToStrMixin, IntEnum):
    """Enum for the different levels of admin access."""

    NORMAL_USER = 0
    CURATOR = 1
    ADMIN = 2
    ADMIN_WITH_DEBUG = 3

    @staticmethod
    def _str_class() -> Enum:
        return AdminLevel


class Species(_StrToIntMixin, Enum):
    """Enumeration of Geneweaver Species."""

    ALL = "All"
    MUS_MUSCULUS = "Mus Musculus"
    HOMO_SAPIENS = "Homo Sapiens"
    RATTUS_NORVEGICUS = "Rattus Norvegicus"
    DANIO_RERIO = "Danio Rerio"
    DROSOPHILA_MELANOGASTER = "Drosophila Melanogaster"
    MACACA_MULATTA = "Macaca Mulatta"
    CAENORHABDITIS_ELEGANS = "Caenorhabditis Elegans"
    SACCHAROMYCES_CEREVISIAE = "Saccharomyces Cerevisiae"
    GALLUS_GALLUS = "Gallus Gallus"
    CANIS_FAMILIARIS = "Canis Familiaris"

    @staticmethod
    def _int_class() -> Enum:
        return SpeciesInt


class SpeciesInt(_IntToStrMixin, IntEnum):
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

    @staticmethod
    def _str_class() -> Enum:
        return Species


class GeneIdentifier(_StrToIntMixin, Enum):
    """Gene Identifier types to match Geneweaver database."""

    ENTREZ = "Entrez"
    ENSEMBLE_GENE = "Ensemble Gene"
    ENSEMBLE_PROTEIN = "Ensemble Protein"
    ENSEMBLE_TRANSCRIPT = "Ensemble Transcript"
    UNIGENE = "Unigene"
    GENE_SYMBOL = "Gene Symbol"
    UNANNOTATED = "Unannotated"
    MGI = "MGI"
    HGNC = "HGNC"
    RGD = "RGD"
    ZFIN = "ZFIN"
    FLYBASE = "FlyBase"
    WORMBASE = "Wormbase"
    SGD = "SGD"
    MIRBASE = "miRBase"
    CGNC = "CGNC"

    @staticmethod
    def _int_class() -> Enum:
        return GeneIdentifierInt


class GeneIdentifierInt(_IntToStrMixin, IntEnum):
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

    @staticmethod
    def _str_class() -> Enum:
        return GeneIdentifier


class Microarray(_StrToIntMixin, Enum):
    """Microarray types (does not match geneweaver database)."""

    AFFYMETRIX_C_ELEGANS_GENOME_ARRAY = "Affymetrix C. elegans Genome Array"
    AFFYMETRIX_DROSOPHILA_GENOME_2_0 = "Affymetrix Drosophila Genome 2.0"
    AFFYMETRIX_HT_HUMAN_GENOME_U133A = "Affymetrix HT Human Genome U133A"
    AFFYMETRIX_HUMAN_35K_SET = "Affymetrix Human 35k Set"
    AFFYMETRIX_HUMAN_35K_SUBA = "Affymetrix Human 35k SubA"
    AFFYMETRIX_HUMAN_35K_SUBB = "Affymetrix Human 35k SubB"
    AFFYMETRIX_HUMAN_35K_SUBC = "Affymetrix Human 35k SubC"
    AFFYMETRIX_HUMAN_35K_SUBD = "Affymetrix Human 35k SubD"
    AFFYMETRIX_HUMAN_GENOME_U133A = "Affymetrix Human Genome U133A"
    AFFYMETRIX_HUMAN_GENOME_U133A_2_0 = "Affymetrix Human Genome U133A 2.0"
    AFFYMETRIX_HUMAN_GENOME_U133B = "Affymetrix Human Genome U133B"
    AFFYMETRIX_HUMAN_GENOME_U133_PLUS_2_0 = "Affymetrix Human Genome U133 Plus 2.0"
    AFFYMETRIX_HUMAN_GENOME_U133_SET = "Affymetrix Human Genome U133 Set"
    AFFYMETRIX_HUMAN_HG_FOCUS_TARGET = "Affymetrix Human HG-Focus Target"
    AFFYMETRIX_MOUSE_EXON_1_0_ST = "Affymetrix Mouse Exon 1.0 ST"
    AFFYMETRIX_MOUSE_EXPRESSION_430A = "Affymetrix Mouse Expression 430A"
    AFFYMETRIX_MOUSE_EXPRESSION_430B = "Affymetrix Mouse Expression 430B"
    AFFYMETRIX_MOUSE_EXPRESSION_430_SET = "Affymetrix Mouse Expression 430 Set"
    AFFYMETRIX_MOUSE_GENE_1_0_ST_ARRAY = "Affymetrix Mouse Gene 1.0 ST Array"
    AFFYMETRIX_MOUSE_GENOME_430_2_0 = "Affymetrix Mouse Genome 430 2.0"
    AFFYMETRIX_MOUSE_GENOME_430A_2_0 = "Affymetrix Mouse Genome 430A 2.0"
    AFFYMETRIX_MURINE_11K_SET = "Affymetrix Murine 11K Set"
    AFFYMETRIX_MURINE_11K_SUBA = "Affymetrix Murine 11K SubA"
    AFFYMETRIX_MURINE_11K_SUBB = "Affymetrix Murine 11K SubB"
    AFFYMETRIX_MURINE_GENOME_U74A = "Affymetrix Murine Genome U74A"
    AFFYMETRIX_MURINE_GENOME_U74B = "Affymetrix Murine Genome U74B"
    AFFYMETRIX_MURINE_GENOME_U74C = "Affymetrix Murine Genome U74C"
    AFFYMETRIX_MURINE_GENOME_U74_SET = "Affymetrix Murine Genome U74 Set"
    AFFYMETRIX_MURINE_GENOME_U74_VERSION_2 = "Affymetrix Murine Genome U74 Version 2"
    AFFYMETRIX_MURINE_GENOME_U74_VERSION_2_SET = (
        "Affymetrix Murine Genome U74 Version 2 Set"
    )
    AFFYMETRIX_RAT_EXON_1_0_ST = "Affymetrix Rat Exon 1.0 ST"
    AFFYMETRIX_RAT_EXPRESSION_230A = "ffymetrix Rat Expression 230A"
    AFFYMETRIX_RAT_EXPRESSION_230B = "ffymetrix Rat Expression 230B"
    AFFYMETRIX_RAT_EXPRESSION_230_SET = "Affymetrix Rat Expression 230 Set"
    AFFYMETRIX_RAT_GENOME_230_2_0 = "Affymetrix Rat Genome 230 2.0"
    AFFYMETRIX_RHESUS_MACAQUE_GENOME = "Affymetrix Rhesus Macaque Genome"
    AFFYMETRIX_YEAST_GENOME_2_0_ARRAY = "Affymetrix Yeast Genome 2.0 Array"
    AFFYMETRIX_YEAST_GENOME_S98_ARRAY = "Affymetrix Yeast Genome S98 Array"
    AFFYMETRIX_ZEBRAFISH_GENOME = "Affymetrix Zebrafish Genome"
    AGILENT_MOUSE_G4121A_TOXICOGENOMICS = "Agilent Mouse G4121A (Toxicogenomics)"
    AGILENT_MOUSE_WHOLE_GENOME_G4122F = "Agilent Mouse Whole Genome G4122F"
    ILLUMINA_HUMAN_6_V2_0 = "Illumina Human-6 v2.0"
    ILLUMINA_MOUSEREF_8_V2_0 = "Illumina MouseRef-8 v2.0"
    ILLUMINA_MOUSEWG_6_V1_1 = "Illumina MouseWG-6 v1.1"
    ILLUMINA_MOUSEWG_6_V2_0 = "Illumina MouseWG-6 v2.0"

    @staticmethod
    def _int_class() -> Enum:
        return MicroarrayInt

    def __str__(self) -> str:
        """Render as a string."""
        return f"microarray {self.value}"


class MicroarrayInt(_IntToStrMixin, IntEnum):
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

    @staticmethod
    def _str_class() -> Enum:
        return Microarray
