from dataclasses import dataclass

from base import BaseStats


@dataclass
class NumericStats(BaseStats):
    def update():
        pass

    def to_dict(self):
        return super().to_dict()
