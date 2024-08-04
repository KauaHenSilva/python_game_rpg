from typing import Optional
from random import randint

from src.enemysClass import EnemyClass

from .ABC_turn import Turn

from src.skills import Skill, DamageSkill, HealingSkill
from src.PlayerClass import PlayerClass
from src.enemysClass import SkeletonMageEnemyClass
from src.utils import getIntUser, separador, pause
from src.status import Status


class TurnPlayer(Turn):
    def __init__(self, player: PlayerClass, enemy: EnemyClass) -> None:
        super().__init__(player, enemy)

    def turn(self, player: PlayerClass, enemy: EnemyClass) -> tuple[PlayerClass, EnemyClass]:
        self.player = player
        self.enemy = enemy

        print("Turno do player\n")
        print(f"{separador}\n")

        relatorio: str = f'\n{separador}\nRelatório:\n\n'

        skill = self.skill_select()

        if skill is None:
            self.end_turn(relatorio)
            return

        relatorio += f'{separador}\n'
        relatorio += f"Você usou a skill {skill.name}\n"

        if isinstance(skill, DamageSkill):
            damage, typeSkill = self.player.skill_cast(skill)
            relatorio += (
                f"Você causou {damage} de dano no inimigo\n"
                f"O tipo de dano foi {typeSkill}\n"
                f"Vida do inimigo: {self.enemy.hpAtual}\n"
            )
            self.enemy.damage_taken(damage, typeSkill)
            relatorio += f"Vida do inimigo após o dano: {self.enemy.hpAtual}\n"

        elif isinstance(skill, HealingSkill):
            heal, typeSkill = self.player.skill_cast(skill)
            relatorio += (
                f"Você curou {heal} de vida\n"
                f"Vida do player: {self.player.hpAtual}\n"
            )
            self.player.life_get(heal)
            relatorio += f"Vida do player após a cura: {self.player.hpAtual}\n"

        self.end_turn(relatorio)
        return self.player, self.enemy

    def skill_select(self) -> Optional[Skill]:
        if not self.player.skill_list_disponivel():
            print("Você não tem skills disponíveis")
            return None

        print("Skills disponíveis:")
        print(f"{separador}")

        for idx, skill in enumerate(self.player.skill_list_disponivel()):
            print(f"Essa skill tem o id: {idx}")
            print(f"{skill}")

        print(f"{separador}")

        valor = getIntUser("Digite o valor da skill: ", 0, len(
            self.player.skill_list_disponivel()) - 1)
        return self.player.skill_list_disponivel()[valor]

    def end_turn(self, relatorio: str) -> None:
        relatorio += f'\n{separador}\n'

        if self.enemy.status == Status.KILLED:
            relatorio += "O Inimigo foi morto\n"
            self.player.xp += self.enemy.xp
            relatorio += f"Você ganhou {self.enemy.xp} de xp\n"
            self.setInimigo(relatorio)
        elif self.player.status == Status.KILLED:
            relatorio += "Você morreu\n"
            print(relatorio)
            pause()
            exit()

        print(relatorio)
        pause()

    def setInimigo(self, relatorio: str):
        self.enemy = SkeletonMageEnemyClass(randint(1, self.player.level))
        relatorio += "Um novo inimigo apareceu\n"
        relatorio += f"{self.enemy}\n"
