from src.PlayerClass import MagoPlayerClass
from src.enemys import SkeletonMageEnemy
from src.turn import TurnPlayer, TurnInimigo, TurnAll
from src.utils import pause
from src.status import Status

player = MagoPlayerClass(5)
enemy = SkeletonMageEnemy(5)

if __name__ == '__main__':
    turnPlayer = TurnPlayer(player, enemy)
    turnInimigo = TurnInimigo(player, enemy)
    turnAll = TurnAll(turnPlayer, turnInimigo)

    while True:
        turnAll.show_stats()
        turnPlayer.turn()

        if enemy.status == Status.ALIVE:
            turnAll.show_stats()
            turnInimigo.turn()
            turnAll.finalizar_turnInimigo()
            
        if player.status == Status.ALIVE:
            turnAll.finalizar_turnPlayer()
            
        pause()
            
        

