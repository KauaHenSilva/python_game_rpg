from abc import ABC, abstractmethod
from typing import Optional

from src.skills import Skill
from src.PlayerClass import PlayerClass
from src.enemysClass import EnemyClass


class Turn(ABC):

    __slots__ = ['_player', '_enemy']

    def __init__(self, player: PlayerClass, enemy: EnemyClass) -> None:
        super().__init__()
        self._player = player
        self._enemy = enemy

    @abstractmethod
    def turn(self, player: PlayerClass, enemy: EnemyClass) -> tuple[PlayerClass, EnemyClass]:
        pass

    @abstractmethod
    def skill_select(self) -> tuple[int, Optional[Skill]]:
        pass

    @abstractmethod
    def end_turn(self, relatorio: str) -> None:
        pass

    @abstractmethod
    def setInimigo(self, relatorio: str):
        pass

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player
