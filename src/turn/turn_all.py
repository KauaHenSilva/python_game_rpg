

from src.utils import separador
from .turn_player import TurnPlayer
from .turn_enemy import TurnEnemy
from src.Class import Class

class TurnAll():

    __slots__ = ['_player', '_enemy', '_turnPlayer', '_turnInimigo']

    def __init__(self, player, enemy) -> None:
        player.set_with_player()
        enemy.set_with_enemy()
        self._player = player
        self._enemy = enemy
        self._turnPlayer: TurnPlayer = TurnPlayer(player, enemy)
        self._turnInimigo: TurnEnemy = TurnEnemy(player, enemy)

    def show_stats(self):
        text = (
            f"\n{separador}\n"
            f"Status dos personagens:\n\n"
            f"Player: {self.player}\n"
            f"Enemy: {self.enemy}\n"
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

    def turn_player(self):
        resp = self.turnPlayer.turn(player=self.player, enemy=self.enemy)
        self.player, self.enemy = resp

    def turn_enemy(self):
        resp = self.turnInimigo.turn(player=self.player, enemy=self.enemy)
        self.player, self.enemy = resp

    @property
    def player(self) -> Class:
        return self._player

    @player.setter
    def player(self, player: Class):
        self._player = player

    @property
    def enemy(self) -> Class:
        return self._enemy

    @enemy.setter
    def enemy(self, enemy: Class):
        self._enemy = enemy

    @property
    def turnPlayer(self) -> TurnPlayer:
        return self._turnPlayer

    @property
    def turnInimigo(self) -> TurnEnemy:
        return self._turnInimigo
