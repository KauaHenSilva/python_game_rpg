from .ABC_skill import Skill, TypeSkill, HealingSkill


class HealSkill(HealingSkill):
    def __init__(self, level=1):
        super().__init__('Heal', 'Cura um aliado ou a si mesmo com eficiência baixa', level)
        self.typeSkill = TypeSkill.MAGICO
        self.setStats()

    def upgrade(self):
        self.level += 1
        self.setStats()

        if self.level == 2:
            self.description = "Cura um aliado ou a si mesmo com eficiência baixa"

        if self.level == 3:
            self.description = "Cura um aliado ou a si mesmo com eficiência media"

        if self.level == 4:
            self.description = "Cura um aliado ou a si mesmo com eficiência máxima"

        if self.level == 5:
            self.description = "Cura um aliado ou a si mesmo com eficiência suprema"

    def setStats(self):
        self.costMP = self.level * 5
        self.healing = self.level * 10

    def skill_cast(self) -> tuple[int, TypeSkill]:
        self.xp += 1
        return self.healing, self.typeSkill

    def action(self):
        return "Heal"

    def __str__(self):
        return super().__str__()
