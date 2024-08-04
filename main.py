from src.PlayerClass import MagoPlayerClass
from src.enemys import SkeletonMageEnemy
from src.turn import TurnPlayer, TurnInimigo, TurnAll
from src.utils import pause
from src.status import Status

player = MagoPlayerClass(1)
enemy = SkeletonMageEnemy(1)

if __name__ == '__main__':
    turnPlayer = TurnPlayer()
    turnInimigo = TurnInimigo()
    turnAll = TurnAll(player, enemy, turnPlayer, turnInimigo)

    while True:
        turnAll.show_stats()
        turnAll.turn_player()

        if enemy.status == Status.ALIVE:
            turnAll.show_stats()
            turnAll.turn_enemy()

        if enemy.status == Status.ALIVE:
            turnAll.finalizar_turnInimigo()

        if player.status == Status.ALIVE:
            turnAll.finalizar_turnPlayer()

        pause()
