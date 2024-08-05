from abc import ABC, abstractmethod
from random import randint
from typing import Optional

from src.skills import Skill
from src.Class import Class, SkeletonMageClass, HumanMageClass, allClass
from src.utils import separador, pause
from src.status import Status


class Turn(ABC):

    __slots__ = ['_player', '_enemy']

    def __init__(self, player: Class, enemy: Class) -> None:
        super().__init__()
        self._player = player
        self._enemy = enemy

    @abstractmethod
    def turn(self, player: Class, enemy: Class) -> tuple[Class, Class]:
        pass

    @abstractmethod
    def skill_select(self) -> tuple[int, Optional[Skill]]:
        pass

    def setInimigo(self, relatorio: str):
        self.enemy = allClass
        self.enemy = self.enemy[randint(0, len(self.enemy) - 1)]
        self.enemy = self.enemy(randint(1, self.player.level + 1))

        self.enemy.set_with_enemy()
        relatorio += "Um novo inimigo apareceu\n"
        relatorio += f"{self.enemy}\n"

    def end_turn(self, relatorio: str) -> None:
        relatorio += f'\n{separador}\n'

        if self.enemy.status == Status.KILLED:
            relatorio += "O Inimigo foi morto\n"
            self.player.xp += self.enemy.xp + 1
            relatorio += f"Você ganhou {self.enemy.xp} de xp\n"
            self.setInimigo(relatorio)
        elif self.player.status == Status.KILLED:
            relatorio += "Você morreu\n"
            print(relatorio)
            pause()
            exit()

        print(relatorio)
        pause()

    @ property
    def player(self):
        return self._player

    @ player.setter
    def player(self, player):
        self._player = player
