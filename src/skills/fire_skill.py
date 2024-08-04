from typing import Union
from .ABC_skill import DamageSkill, Skill, TypeSkill


class FireSkill(DamageSkill):
    def __init__(self, level=1):
        super().__init__('Fireball', 'Shoot a fireball', level)
        self.typeSkill = TypeSkill.MAGICO
        self.setStats()

    def action(self):
        return "Fireball"

    def upgrade(self):
        self.level += 1
        self.setStats()

        if self.level == 2:
            self.description = "Shoot a bigger fireball"

        if self.level == 3:
            self.description = "Shoot a huge fireball"

        if self.level == 4:
            self.description = "Shoot a massive fireball"

        if self.level == 5:
            self.description = "Shoot a gigantic fireball"

    def setStats(self):
        self.costMP = self.level * 5
        self.damage = self.level * 10

    def skill_cast(self) -> tuple[int, TypeSkill]:
        self.xp += 1
        return self.damage, self.typeSkill

    def __str__(self):
        return super().__str__()
