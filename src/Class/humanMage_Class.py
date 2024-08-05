from src.skills import FireSkill, HealSkill, TypeSkill, Skill, HealingSkill, DamageSkill
from .ABC_Class import Class

from random import randint


class HumanMageClass(Class):
    def __init__(self, level: int = 1):
        super().__init__('Mago Humano', level, 'Mago é um ser que pratica magia')
        self.skills = [FireSkill(1), HealSkill(1)]
        self.setStats()

    def damage_taken(self, damage, typeSkill: TypeSkill):
        if typeSkill == TypeSkill.MAGICO:
            self.hpAtual -= int(damage / 2)
        else:
            self.hpAtual -= damage

    def skill_cast(self, skill: Skill) -> tuple[int, TypeSkill]:
        if (skill.typeSkill == TypeSkill.MAGICO):
            self.mpAtual -= int(skill.costMP / 2)
            self.stAtual -= skill.costST
        else:
            self.mpAtual -= skill.costMP
            self.stAtual -= skill.costST

        if isinstance(skill, DamageSkill):
            damage, typeSkill = skill.skill_cast()

            damage = randint(damage - 5, damage + 5)

            if typeSkill == TypeSkill.MAGICO:
                return int(damage), typeSkill
            return int(damage / 2), typeSkill

        if isinstance(skill, HealingSkill):
            heal, typeSkill = skill.skill_cast()

            heal = randint(heal - 5, heal + 5)

            if typeSkill == TypeSkill.MAGICO:
                return int(heal), typeSkill
            return int(heal / 2), typeSkill

        return 0, TypeSkill.MAGICO

    def setStats(self):
        self.hpRegen = self.level * 2
        self.mpRegen = 5 + self.level * 2
        self.stRegen = self.level

        self.hpMax = 100 + (self.level * 10)
        self.mpMax = 50 + (self.level * 10)
        self.stMax = 20 + (self.level * 5)

        self.hpAtual = self.hpMax
        self.mpAtual = self.mpMax
        self.stAtual = self.stMax

        self.xp = (self.level * 100)

    def life_get(self, life_get):
        self.hpAtual += life_get

    def next_turn(self):
        self.hpAtual += self.hpRegen
        self.mpAtual += self.mpRegen
        self.stAtual += self.stRegen

        print(
            f"O {self.name} recuperou {self.hpRegen} de HP, {self.mpRegen} de MP e {self.stRegen} de ST\n")

    def set_with_enemy(self):
        self.xp = self.level * 100
        self.skills = [FireSkill(randint(1, self.level)),
                       HealSkill(randint(1, self.level)),]

    def set_with_player(self):
        self.xp = 0
