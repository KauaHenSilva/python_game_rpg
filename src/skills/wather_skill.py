from typing import Union
from .ABC_skill import DamageSkill, Skill, TypeSkill


class WatherSkill(DamageSkill):
    def __init__(self, level=1):
        super().__init__('Jato d\'água', 'Lança um jato d\'água', level)
        self.typeSkill = TypeSkill.MAGICO
        self.setStats()

    def action(self):
        return "Jato d'água boladão"

    def upgrade(self):
        self.level += 1
        self.setStats()

    def setStats(self):
        self.costMP = self.level * 17
        self.damage = self.level * 15

    def skill_cast(self) -> tuple[int, TypeSkill]:
        self.xp += 1
        return self.damage, self.typeSkill

    def __str__(self):
        return super().__str__()
