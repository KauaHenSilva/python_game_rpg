from abc import ABC, abstractmethod
from enum import Enum
from random import randint
from typing import Union

from src.skills.ABC_skill import Skill, TypeSkill
from src.status import Status


class Inimigo(ABC):

    __slots__ = ['_name', '_level', '_descricao', '_hpMax',
                 '_mpMax', '_stMax', '_hpAtual', '_mpAtual', '_stAtual', '_status', '_xp', '_skills']

    def __init__(self, nameClass, level, descricao) -> None:
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

    def skill_list_disponivel(self) -> list[Skill]:
        skills_disponiveis = []
        for skill in self.skills:
            if skill.costMP <= self.mpAtual and skill.costST <= self.stAtual:
                skills_disponiveis.append(skill)
        return skills_disponiveis

    def skill_select(self) -> Union[Skill, None]:
        skill_possivel = []
        for skill in self.skills:
            if skill.costMP <= self.mpAtual and skill.costST <= self.stAtual:
                skill_possivel.append(skill)

        if not skill_possivel:
            return None

        skillCast = skill_possivel[randint(0, len(skill_possivel) - 1)]
        return skillCast
    
    @property
    def hpRegen(self):
        return self._hpRegen
    
    @hpRegen.setter
    def hpRegen(self, value):
        if not isinstance(value, int):
            raise ValueError("HP Regen deve ser um inteiro")
        
        if value < 0:
            print("HP Regen não pode ser negativo")
            return
        
        self._hpRegen = value
    
    @property
    def mpRegen(self):
        return self._mpRegen
    
    @mpRegen.setter
    def mpRegen(self, value):
        if not isinstance(value, int):
            raise ValueError("MP Regen deve ser um inteiro")
        
        if value < 0:
            print("MP Regen não pode ser negativo")
            return
        
        self._mpRegen = value
    
    @property
    def stRegen(self):
        return self._stRegen

    @stRegen.setter
    def stRegen(self, value):
        if not isinstance(value, int):
            raise ValueError("ST Regen deve ser um inteiro")

        if value < 0:
            print("ST Regen não pode ser negativo")
            return

        self._stRegen = value

    @property
    def skills(self) -> list[Skill]:
        return self._skills

    @skills.setter
    def skills(self, value):
        if not isinstance(value, list):
            raise ValueError("Skills deve ser uma lista de Skills")

        self._skills = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, Status):
            raise ValueError("Status deve ser um Status")
        self._status = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if not isinstance(value, int):
            raise ValueError("XP deve ser um inteiro")

        if value < 0:
            print("XP não pode ser negativo")
            return

        self._xp = value

    @property
    def hpAtual(self):
        return self._hpAtual

    @hpAtual.setter
    def hpAtual(self, value):
        if not isinstance(value, int):
            raise ValueError("HP deve ser um inteiro")

        if value <= 0:
            self._status = Status.KILLED
            self._hpAtual = 0
            return

        self._hpAtual = value

    @property
    def mpAtual(self):
        return self._mpAtual

    @mpAtual.setter
    def mpAtual(self, value):
        if not isinstance(value, int):
            raise ValueError("MP deve ser um inteiro")

        if value < 0:
            print("MP não pode ser negativo")
            return

        self._mpAtual = value

    @property
    def stAtual(self):
        return self._stAtual

    @stAtual.setter
    def stAtual(self, value):
        if not isinstance(value, int):
            raise ValueError("ST deve ser um inteiro")

        if value < 0:
            print("ST não pode ser negativo")
            return

        self._stAtual = value

    @property
    def hpMax(self):
        return self._hpMax

    @hpMax.setter
    def hpMax(self, value):
        if not isinstance(value, int):
            raise ValueError("HP deve ser um inteiro")

        if value < 0:
            print("HP não pode ser negativo")
            return

        self._hpMax = value

    @property
    def mpMax(self):
        return self._mpMax

    @mpMax.setter
    def mpMax(self, value):
        if not isinstance(value, int):
            raise ValueError("MP deve ser um inteiro")

        if value < 0:
            print("MP não pode ser negativo")
            return

        self._mpMax = value

    @property
    def stMax(self):
        return self._stMax

    @stMax.setter
    def stMax(self, value):
        if not isinstance(value, int):
            raise ValueError("ST deve ser um inteiro")

        if value < 0:
            print("ST não pode ser negativo")
            return

        self._stMax = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Nome deve ser uma string")

        if len(value) < 3:
            print("Nome deve ter pelo menos 3 caracteres")
            return

        self._name = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        if not isinstance(value, str):
            raise ValueError("Descrição deve ser uma string")

        if len(value) < 3:
            print("Descrição deve ter pelo menos 3 caracteres")
            return

        self._descricao = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise ValueError("Nivel deve ser um inteiro")

        if value > 5:
            print("Nivel deve ser no máximo 5")
            return

        if value < 1:
            print("Nivel deve ser no mínimo 1")
            return

        self.setStats()
        self._level = value

    def __str__(self):
        skills_all = ', '.join(
            [f'{skill.name} (level {skill.level})' for skill in self.skills])

        exibir = (
            f"Nome: {self.name}\n"
            f"Level: {self.level}\n"
            f"HP: {self.hpAtual}/{self.hpMax}\n"
            f"MP: {self.mpAtual}/{self.mpMax}\n"
            f"ST: {self.stAtual}/{self.stMax}\n"
            f"XP: {self.xp}\n"
            f"Skills: {skills_all}\n"
        )

        return f'{exibir}'
