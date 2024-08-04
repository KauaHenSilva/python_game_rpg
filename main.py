from src.PlayerClass import MagoPlayerClass
from src.enemysClass import SkeletonMageEnemyClass
from src.turn import TurnPlayer, TurnEnemy, TurnAll
from src.utils import pause
from src.status import Status

player = MagoPlayerClass(1)
enemy = SkeletonMageEnemyClass(1)

if __name__ == '__main__':
    turnPlayer = TurnPlayer(player, enemy)
    turnInimigo = TurnEnemy(player, enemy)
    turnAll = TurnAll(player, enemy, turnPlayer, turnInimigo)

    while True:
        turnAll.show_stats()
        turnAll.turn_player()

        if turnAll.enemy.status == Status.ALIVE:
            turnAll.show_stats()
            turnAll.turn_enemy()

        if turnAll.enemy.status == Status.ALIVE:
            turnAll.finalizar_turnInimigo()

        if turnAll.player.status == Status.ALIVE:
            turnAll.finalizar_turnPlayer()

        pause()
