from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseStats(ABC):
    @abstractmethod
    def update():
        pass

    @abstractmethod
    def to_dict(self):
        pass
