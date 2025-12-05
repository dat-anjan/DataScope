import gc
from abc import ABC, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict

import pandas as pd


class ColTypes(Enum):
    CAT = auto()
    NUM = auto()
    ORD = auto()


@dataclass
class DSCols:
    categorical: list[str] = field(default_factory=list)
    numerical: list[str] = field(default_factory=list)
    ordinal: list[str] = field(default_factory=list)


@dataclass
class DSMeta:
    record_count: int
    col_count: int
    col_types: Dict[str, str]


@dataclass
class BaseStats(ABC):
    @abstractmethod
    def update(self):
        pass


@dataclass
class DSTable:
    path: str
    name: str = "unnamed"
    df: pd.DataFrame = field(init=False)
    id_col: str | int = -1
    cols: DSCols = field(default_factory=lambda: DSCols())
    metadata: DSMeta = field(init=False)
    last_row: int = -1

    @contextmanager
    def load(self, chunk_size=100000):
        try:
            df = pd.read_csv(self.path, nrows=chunk_size, skiprows=self.last_row + 1)
            yield df
        finally:
            del df
            gc.collect()


data = DSTable(name="table", path=r"input.csv")

with data.load() as df:
    data.update_stats(df)
