"""A module for common complex types used by Geneweaver."""

from pathlib import Path
from typing import Dict, Union

StringOrPath = Union[str, Path]

DictRow = Dict[str, Union[str, int]]
