from random import randint
from src.turn import TurnAll
from src.utils import pause
from src.status import Status

from src.Class import HumanMageClass, SkeletonMageClass, allClass

player = allClass[randint(0, len(allClass) - 1)]()
enemy = allClass[randint(0, len(allClass) - 1)]()

if __name__ == '__main__':
    print("Bem vindo ao jogo\n")
    
    print("Classes Sorteadas:\n")
    
    if(randint(0, 1)):
        print(player)
        print(enemy)
    else:
        print(enemy)
        print(player)
        
    pause()

    turnAll = TurnAll(player, enemy)

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
