from abc import ABC, abstractmethod
from typing import Union

from src.skills import Skill, TypeSkill
from src.status import Status


class PlayerClass(ABC):

    __slots__ = ['_nameClass', '_level', '_descrisao', '_hpMax', '_mpMax',
                 '_stMax', '_xp', '_points', '_hpAtual', '_mpAtual', '_stAtual', '_skills', '_status']

    def __init__(self, nameClass, level, descrisao) -> None:
        self._status = Status.ALIVE
        self._nameClass = nameClass
        self._descrisao = descrisao
        
        self._xp: int = 0
        
        self._hpMax: int = 100
        self._mpMax: int = 100
        self._stMax: int = 100
        
        self._hpAtual: int
        self._mpAtual: int
        self._stAtual: int
        
        self._hpRegen: int = 5
        self._mpRegen: int = 5
        self._stRegen: int = 5
        
        self._level = level
        self._xp = 0
        self._points = 0
        self._skills = []

    @abstractmethod
    def setStats(self):
        pass

    @abstractmethod
    def life_get(self, life_get):
        pass

    @abstractmethod
    def damage_taken(self, damage, typeSkill: TypeSkill):
        pass


    @abstractmethod
    def skill_cast(self, skill) -> tuple[int, TypeSkill]:
        pass
    
    
    @abstractmethod
    def next_turn(self):
        pass
    
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
    
    def skill_list_disponivel(self) -> list[Skill]:
        skills_disponiveis = []
        for skill in self.skills:
            if skill.costMP <= self.mpAtual and skill.costST <= self.stAtual:
                skills_disponiveis.append(skill)
        return skills_disponiveis
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, Status):
            raise ValueError("Status deve ser um Status")

        self._status = value

    @property
    def skills(self) -> list[Skill]:
        return self._skills

    @skills.setter
    def skills(self, value):
        if not isinstance(value, list):
            raise ValueError("Skills deve ser uma lista de Skills")

        self._skills = value

    def add_points_to_stats(self):
        if self.points == 0:
            print("Você não tem pontos suficientes")
            return

        while self.points > 0:
            print("Escolha a habilidade que deseja aumentar:\n1 - HP\n2 - MP\n3 - ST")
            option = input()
            if option == '1':
                self.hpMax += 10
            elif option == '2':
                self.mpMax += 10
            elif option == '3':
                self.stMax += 10
            else:
                print("Opção inválida")
                continue
            points -= 1

        self.points -= points

    @property
    def nameClass(self):
        return self._nameClass

    @nameClass.setter
    def nameClass(self, value):
        if not isinstance(value, str):
            raise ValueError("Nome deve ser uma string")

        if len(value) < 3:
            print("Nome deve ter pelo menos 3 caracteres")
            return

        self._nameClass = value

    @property
    def descrisao(self):
        return self._descrisao

    @descrisao.setter
    def descrisao(self, value):
        if not isinstance(value, str):
            raise ValueError("Descrição deve ser uma string")

        if len(value) < 3:
            print("Descrição deve ter pelo menos 3 caracteres")
            return

        self._descrisao = value

    @property
    def hpMax(self):
        return self._hpMax

    @hpMax.setter
    def hpMax(self, value):
        if not isinstance(value, int):
            raise ValueError("HP deve ser um inteiro")

        self._hpMax = value

    @property
    def mpMax(self):
        return self._mpMax

    @mpMax.setter
    def mpMax(self, value):
        if not isinstance(value, int):
            raise ValueError("MP deve ser um inteiro")

        if value < 1:
            print("MP deve ser no mínimo 1")
            return

        self._mpMax = value

    @property
    def stMax(self):
        return self._stMax

    @stMax.setter
    def stMax(self, value):
        if not isinstance(value, int):
            raise ValueError("ST deve ser um inteiro")

        if value < 1:
            print("ST deve ser no mínimo 1")
            return

        self._stMax = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        
        if not isinstance(value, int):
            raise ValueError("XP deve ser um inteiro")

        if self._xp > value:
            print("XP não pode ser menor que o valor atual")
            return

        if value < 0:
            print("A quantidade de xp ganha não deve ser negativa")
            return
        
        if self.level == 5:
            return

        if value >= 100 * self.level:
            while value >= 100 * self.level:
                value -= 100 * self.level
                self.level += 1
                self.setStats()

        self._xp = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if not isinstance(value, int):
            raise ValueError("Points deve ser um inteiro")

        self._points = value

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

        self.hpAtual = self.hpMax
        self.mpAtual = self.mpMax
        self.stAtual = self.stMax

        self._level = value

    @property
    def hpAtual(self):
        return self._hpAtual

    @hpAtual.setter
    def hpAtual(self, value):
        if not isinstance(value, int):
            raise ValueError("HP deve ser um inteiro")

        if value <= 0:
            self.status = Status.KILLED
            self._hpAtual = 0
            return

        if value > self._hpMax:
            self._hpAtual = self._hpMax
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
            print("Você está sem mana")
            self._mpAtual = 0
            return

        if value > self._mpMax:
            self._mpAtual = self._mpMax
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
            print("Você está sem stamina")
            self._stAtual = 0
            return

        if value > self._stMax:
            self._stAtual = self._stMax
            return

        self._stAtual = value

    def __str__(self):
        skills_all = ', '.join(
            [f'{skill.name} (level {skill.level})' for skill in self.skills])

        exibir = (
            f"Nome: {self.nameClass}\n"
            f"Level: {self.level}\n"
            f"HP: {self.hpAtual}/{self.hpMax}\n"
            f"MP: {self.mpAtual}/{self.mpMax}\n"
            f"ST: {self.stAtual}/{self.stMax}\n"
            f"XP: {self.xp}\n"
            f"Skills: {skills_all}\n"
        )

        return f'{exibir}'
