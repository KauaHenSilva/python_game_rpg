from .ABC_skill import Skill, TypeSkill, HealingSkill


class HealSkill(HealingSkill):
    def __init__(self, level=1):
        super().__init__('Cura', 'Cura um aliado ou a si mesmo', level)
        self.typeSkill = TypeSkill.MAGICO
        self.setStats()

    def action(self):
        return "Cura"

    def upgrade(self):
        self.level += 1
        self.setStats()

    def setStats(self):
        self.costMP = self.level * 20
        self.healing = self.level * 10

    def skill_cast(self) -> tuple[int, TypeSkill]:
        self.xp += 1
        return self.healing, self.typeSkill

    def __str__(self):
        return super().__str__()
