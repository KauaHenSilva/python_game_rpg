

from src.utils import separador
from .turn_player import TurnPlayer
from .turn_enemy import TurnInimigo


class TurnAll():
    def __init__(self, turnPlayer: TurnPlayer, turnInimigo: TurnInimigo) -> None:
        self.turnPlayer = turnPlayer
        self.turnInimigo = turnInimigo

    def show_stats(self):
        text = (
            f"\n{separador}\n"
            f"Status dos personagens:\n\n"
            f"Player: \n{self.turnPlayer.player}\n"
            f"Enemy: \n{self.turnInimigo.enemy}\n"
            f"{separador}"
        )
        print(text)

    def finalizar_turnPlayer(self):
        print(f"{separador}", end='')
        print("Finalizando turno do player")
        print(f"{separador}", end='')
        self.turnPlayer.player.next_turn()

    def finalizar_turnInimigo(self):
        print(f"{separador}", end='')
        print("Finalizando turno do inimigo")
        print(f"{separador}", end='')
        self.turnInimigo.enemy.next_turn()
