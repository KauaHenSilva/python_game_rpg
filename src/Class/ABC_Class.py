from abc import ABC, abstractmethod
from typing import Union

from src.skills import TypeSkill
from src.status import Status


class Class(ABC):

    __slots__ = ['_nameClass', '_level', '_descrisao', '_hpMax', '_mpMax',
                 '_stMax', '_xp', '_points', '_hpAtual', '_mpAtual', '_stAtual', '_skills', '_status']

    def __init__(self, nameClass, level, descricao) -> None:
        super().__init__()

        self._status: Status = Status.ALIVE
        self._name: str = nameClass
        self._level: int = level
        self._descricao: str = descricao

        self._xp: int = 10
        self._hpMax: int = 100
        self._mpMax: int = 50
        self._stMax: int = 50

        self._hpRegen: int = 5
        self._mpRegen: int = 5
        self._stRegen: int = 5

        self._skills = []

        self._hpAtual: int = self._hpMax
        self._mpAtual: int = self._mpMax
        self._stAtual: int = self._stMax

    @abstractmethod
    def damage_taken(self, damage, typeDamage):
        pass

    @abstractmethod
    def skill_cast(self, skill) -> tuple[int, Union[TypeSkill, None]]:
        pass

    @abstractmethod
    def setStats(self):
        pass

    @abstractmethod
    def life_get(self, life_get):
        pass

    @abstractmethod
    def next_turn(self):
        pass
