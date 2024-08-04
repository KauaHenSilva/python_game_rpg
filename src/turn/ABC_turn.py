from abc import ABC, abstractmethod
from typing import Optional

from src.skills import Skill
from src.PlayerClass import PlayerClass
from src.enemys import Inimigo


class Turn(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def turn(self, player: PlayerClass, enemy: Inimigo) -> tuple[PlayerClass, Inimigo]:
        pass

    @abstractmethod
    def skill_select(self) -> tuple[int, Optional[Skill]]:
        pass
