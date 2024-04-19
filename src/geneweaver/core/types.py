"""A module for common complex types used by Geneweaver."""

from pathlib import Path
from typing import Dict, List, Union

from geneweaver.core.schema.gene import GeneValue

StringOrPath = Union[str, Path]

DictRow = Dict[str, Union[str, int]]

GeneIds = List[str]

GeneIdValues = List[GeneValue]

StrainIds = List[str]
