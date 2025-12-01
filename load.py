from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict


class ColTypes(Enum):
    CAT = auto()
    NUM = auto()
    ORD = auto()


@dataclass
class DSCols:
    categorical: list[str] = field(default_factory=list)
    numerical: list[str] = field(defualt_factory=list)
    ordinal: list[str] = field(default_factory=list)


@dataclass
class DSMeta:
    record_count: int
    col_count: int
    col_types: Dict[str, str]


@dataclass
class DSTable:
    name: str = field(default_factory=lambda: "unnamed")
    id: str | int = field(default_factory=lambda: -1)
    cols: DSCols = field(default_factory=DSCols)

    def __post_init__(self):
        assert len(self.cols.categorical)
