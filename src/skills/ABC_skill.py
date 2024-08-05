from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

class TypeSkill(Enum):
    FISICO = 1
    MAGICO = 2

    def __str__(self):
        return self.name.capitalize()


class Skill(ABC):

    __slots__ = ['_name', '_description', '_level',
                 '_costMP', '_costST', '_typeSkill', '_xp']

    def __init__(self, name, description, level):
        self._name: str = name
        self._description: str = description
        self._level: int = level
        self._typeSkill: TypeSkill
        self._costMP: int = 0
        self._costST: int = 0
        self._xp: int = 0
        
    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def upgrade(self):
        pass

    @abstractmethod
    def setStats(self):
        pass

    @abstractmethod
    def skill_cast(self) -> tuple[int, TypeSkill]:
        pass

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if not isinstance(value, int):
            raise ValueError("XP must be an integer")
        if value < 0:
            raise ValueError("XP must be at least 0")

        value_temp = value

        if value_temp >= 10 * self.level:
            value_temp = value_temp - 10 * self.level
            self.upgrade()

        self._xp = value_temp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")

        if len(value) < 3:
            print("Name must be at least 3 characters long")
            return

        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")

        if len(value) < 3:
            print("Description must be at least 3 characters long")
            return

        self._description = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise ValueError("Level must be an integer")

        if value < 1:
            print("Level must be at least 1")
            return

        if value > 5:
            print("Level must be at most 5")
            return

        self.setStats()
        self._level = value

    @property
    def costMP(self):
        return self._costMP

    @costMP.setter
    def costMP(self, value):
        if not isinstance(value, int):
            raise ValueError("Cost must be an integer")

        if value < 0:
            print("Cost must be at least 0")
            return

        self._costMP = value

    @property
    def costST(self):
        return self._costST

    @costST.setter
    def costST(self, value):
        if not isinstance(value, int):
            raise ValueError("Cost must be an integer")

        if value < 0:
            print("Cost must be at least 0")
            return

        self._costST = value

    @property
    def typeSkill(self):
        return self._typeSkill

    @typeSkill.setter
    def typeSkill(self, value):
        if not isinstance(value, TypeSkill):
            raise ValueError("O tipo deve ser um TypeSkill")

        self._typeSkill = value

    def __str__(self) -> str:
        text = (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Level: {self.level}\n"
            f"Cost MP: {self.costMP}\n"
            f"Cost ST: {self.costST}\n"
            f"Type Skill: {self.typeSkill}\n"
            f"XP: {self.xp}\n"
            f"Action: {self.action()}\n"
        )
        return text


class DamageSkill(Skill):
    __slots__ = ['_damage']

    def __init__(self, name, description, level):
        super().__init__(name, description, level)
        self._damage: int = 0

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if not isinstance(value, int):
            raise ValueError("Damage must be an integer")
        if value < 0:
            raise ValueError("Damage must be at least 0")

        self._damage = value

    def __str__(self) -> str:
        text = (
            f"{super().__str__()}"
            f"Damage: {self.damage}\n"
        )
        return text


class HealingSkill(Skill):
    __slots__ = ['_healing']

    def __init__(self, name, description, level):
        super().__init__(name, description, level)
        self._healing: int = 0

    @property
    def healing(self):
        return self._healing

    @healing.setter
    def healing(self, value):
        if not isinstance(value, int):
            raise ValueError("Healing must be an integer")
        if value < 0:
            raise ValueError("Healing must be at least 0")
        self._healing = value

    def __str__(self) -> str:
        text = (
            f"{super().__str__()}"
            f"healing: {self.healing}\n"
        )
        return text