from random import randint
from typing import Union
from src.skills.ABC_skill import HealingSkill, Skill, DamageSkill
from src.skills.fire_skill import FireSkill
from .ABC_Enemys import Inimigo
from src.skills.ABC_skill import TypeSkill


class SkeletonMageEnemy(Inimigo):
    def __init__(self, level):
        super().__init__('Skeleton', level, 'A skeleton that will')
        self.setStats()
        
    def damage_taken(self, damage, typeDamage: TypeSkill):
        if typeDamage == TypeSkill.FISICO:
            self.hpAtual -= damage
        elif typeDamage == TypeSkill.MAGICO:
            self.hpAtual -= int(damage * 0.5)

    def life_get(self, life_get):
        self.hpAtual -= life_get

    def setStats(self):
        self.mpRegen = self.level * 2
        self.stRegen = self.level
        
        self.hpMax = 50 + (self.level * 10)
        self.mpMax = 10 + (self.level * 5)
        self.stMax = 10 + (self.level * 5)
        self.xp = (self.level * 100)
        
        self.hpAtual = self.hpMax
        self.mpAtual = self.mpMax
        self.stAtual = self.stMax

        self.skills = [FireSkill(randint(1, self.level))]

    def skill_cast(self, skill) -> tuple[int, Union[TypeSkill, None]]:
        if skill is None:
            raise ValueError("Skill não pode ser None")

        if self.mpAtual < skill.costMP or self.stAtual < skill.costST:
            return 0, None

        if skill.typeSkill == TypeSkill.MAGICO:
            self.mpAtual -= int(skill.costMP / 2)
            self.stAtual -= skill.costST
        else:
            self.mpAtual -= skill.costMP
            self.stAtual -= skill.costST

        if isinstance(skill, DamageSkill):
            damage, typeSkill = skill.skill_cast()
            if typeSkill == TypeSkill.MAGICO:
                return int(damage), skill.typeSkill
            return int(damage * 0.5), skill.typeSkill
        
        return 0, None

    def next_turn(self):
        self.mpAtual += self.mpRegen
        self.stAtual += self.stRegen

        print(f'{self.name} recuperou {self.mpRegen} de MP e {self.stRegen} de ST\n')
