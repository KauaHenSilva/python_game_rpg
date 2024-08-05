from typing import Optional
from random import randint

from .ABC_turn import Turn

from src.skills import Skill, DamageSkill, HealingSkill, TypeSkill
from src.utils import separador, pause
from src.status import Status

from src.Class import Class


class TurnEnemy(Turn):
    def __init__(self, player: Class, enemy: Class) -> None:
        super().__init__(player, enemy)

    def turn(self, player: Class, enemy: Class) -> tuple[Class, Class]:
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
