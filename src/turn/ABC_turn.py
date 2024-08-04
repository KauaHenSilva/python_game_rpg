from abc import ABC, abstractmethod
from typing import Optional

from src.skills import Skill
from src.PlayerClass import PlayerClass
from src.enemys import Inimigo


class Turn(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def turn(self):
        pass
    
    @abstractmethod
    def skill_select(self) -> tuple[int, Optional[Skill]]:
        pass
    
    @property
    def player(self) -> PlayerClass:
        return self._player
    
    @property
    def enemy(self) -> Inimigo:
        return self._enemy
    
    @enemy.setter
    def enemy(self, enemy):
        self._enemy = enemy
