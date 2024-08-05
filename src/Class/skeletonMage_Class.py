from random import randint
from typing import Union
from src.skills import DamageSkill, TypeSkill
from src.skills import FireSkill, DirtSkill
from .ABC_Class import Class


class SkeletonMageClass(Class):
    def __init__(self, level=1):
        super().__init__('Esqueleto Mago', level, 'Um esqueleto que pratica magia')
        self.skills = [FireSkill(1), DirtSkill(1)]
        self.setStats()

    def damage_taken(self, damage, typeDamage: TypeSkill):
        if typeDamage == TypeSkill.FISICO:
            self.hpAtual -= damage
        elif typeDamage == TypeSkill.MAGICO:
            print(f"A Classe {self.name} recebe menos dano com magia")
            print(f"O dano recebido foi de {int(damage / 2)}")
            self.hpAtual -= int(damage * 0.5)

    def life_get(self, life_get):
        self.hpAtual -= life_get

    def setStats(self):
        self.hpRegen = self.level
        self.mpRegen = 5 + self.level * 2
        self.stRegen = self.level

        self.hpMax = 100 + (self.level * 10) + (self.level * 2)
        self.mpMax = 50 + (self.level * 10)
        self.stMax = 20 + (self.level * 5)

        self.hpAtual = self.hpMax
        self.mpAtual = self.mpMax
        self.stAtual = self.stMax

    def skill_cast(self, skill) -> tuple[int, Union[TypeSkill, None]]:
        if skill is None:
            raise ValueError("Skill não pode ser None")

        if self.mpAtual < skill.costMP or self.stAtual < skill.costST:
            return 0, None

        if skill.typeSkill == TypeSkill.MAGICO:
            print(f"A Classe {self.name} gasta menos MP com magia")
            print(f"O mp gasto foi de {int(skill.costMP / 2)}")

            self.mpAtual -= int(skill.costMP / 2)
            self.stAtual -= skill.costST
        else:
            self.mpAtual -= skill.costMP
            self.stAtual -= skill.costST

        if isinstance(skill, DamageSkill):
            damage, typeSkill = skill.skill_cast()

            if typeSkill == TypeSkill.MAGICO:
                print(f"A Classe {self.name} causa mais dano com magia")
                print(f"O dano causado foi de {int(damage * 2)}")
                return int(damage * 2), skill.typeSkill

            print(f"A Classe {self.name} causa menos dano com fisico")
            print(f"O dano causado foi de {int(damage / 2)}")
            return int(damage * 0.5), skill.typeSkill

        return 0, None

    def next_turn(self):
        self.mpAtual += self.mpRegen
        self.stAtual += self.stRegen

        print(f'{self.name} recuperou {self.mpRegen} de MP e {self.stRegen} de ST\n')

    def set_with_enemy(self):
        self.xp = self.level * 100
        self.skills = [FireSkill(randint(1, self.level))]

    def set_with_player(self):
        self.xp = 0
