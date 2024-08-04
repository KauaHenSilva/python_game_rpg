from typing import Optional
from random import randint

from .ABC_turn import Turn

from src.skills import Skill, DamageSkill, HealingSkill, TypeSkill
from src.PlayerClass import PlayerClass
from src.enemysClass import EnemyClass, SkeletonMageEnemyClass
from src.utils import separador, pause
from src.status import Status


class TurnEnemy(Turn):
    def __init__(self, player: PlayerClass, enemy: EnemyClass) -> None:
        super().__init__(player, enemy)
        

    def turn(self, player: PlayerClass, enemy: EnemyClass) -> tuple[PlayerClass, EnemyClass]:
        self.player = player
        self.enemy = enemy

        print("Turno do Inimigo\n")
        print(f"{separador}\n")

        relatorio: str = 'Relatório:\n\n'

        skill = self.skill_select()

        if skill is None:
            self.end_turn(relatorio)
            return

        relatorio += f'{separador}\n'
        relatorio += f"O inimigo usou a skill {skill.name}\n"

        if isinstance(skill, DamageSkill):
            damage, typeSkill = self.enemy.skill_cast(skill)
            relatorio += (
                f"O inimigo causou {damage} de dano BRUTO no player\n"
                f"O tipo de dano foi {typeSkill}\n"
                f"Vida do player atualmente: {self.player.hpAtual}\n"
            )
            self.player.damage_taken(damage, typeSkill)
            relatorio += f"Vida do player após o dano: {self.player.hpAtual}\n"

        elif isinstance(skill, HealingSkill):
            heal, typeSkill = self.enemy.skill_cast(skill)
            relatorio += (
                f"O inimigo curou {heal} de vida\n"
                f"Vida do inimigo: {self.enemy.hpAtual}\n"
            )
            self.enemy.life_get(heal)
            relatorio += f"Vida do inimigo após a cura: {self.enemy.hpAtual}\n"

        self.end_turn(relatorio)

        return self.player, self.enemy

    def skill_select(self) -> Optional[Skill]:
        if not self.enemy.skill_list_disponivel():
            print("O inimigo não pode usar skill")
            return None

        print("Skills disponíveis:")
        print(f"{separador}")

        for idx, skill in enumerate(self.enemy.skill_list_disponivel()):
            print(f"Essa skill tem o id: {idx}")
            print(f"{skill}")

        print(f"{separador}")

        skill = self.enemy.skill_select()
        return skill

    def end_turn(self, relatorio: str) -> None:
        relatorio += f'\n{separador}\n'

        if self.enemy.status == Status.KILLED:
            relatorio += "O Inimigo foi morto\n"
            self.player.xp += self.enemy.xp
            relatorio += f"Você ganhou {self.enemy.xp} de xp\n"
            self.setInimigo(relatorio)
        elif self.player.status == Status.KILLED:
            relatorio += "Você foi morto\n"
            print(relatorio)
            pause()
            exit()

        print(relatorio)
        pause()

    def setInimigo(self, relatorio: str):
        self.enemy = SkeletonMageEnemyClass(randint(1, self.player.level))
        relatorio += "Um novo inimigo apareceu\n"
        relatorio += f"{self.enemy}\n"
