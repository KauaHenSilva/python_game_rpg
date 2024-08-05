from typing import Union
from .ABC_skill import DamageSkill, Skill, TypeSkill


class FireSkill(DamageSkill):
    def __init__(self, level=1):
        super().__init__('Bola de fogo', 'Lança uma bola de fogo', level)
        self.typeSkill = TypeSkill.MAGICO
        self.setStats()

    def action(self):
        return "Fireball"

    def upgrade(self):
        self.level += 1
        self.setStats()

    def setStats(self):
        self.costMP = self.level * 5
        self.damage = self.level * 12

    def skill_cast(self) -> tuple[int, TypeSkill]:
        self.xp += 1
        return self.damage, self.typeSkill

    def __str__(self):
        return super().__str__()
