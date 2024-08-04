import unittest
from unittest.mock import patch
from src.turn.turn_player import TurnPlayer
from src.skills import DamageSkill, HealingSkill, TypeSkill, FireSkill, HealSkill
from src.PlayerClass import PlayerClass, MagoPlayerClass
from src.enemysClass import Inimigo, SkeletonMageEnemy
from src.status import Status


class TestTurnPlayer(unittest.TestCase):
    def setUp(self):
        self.player = MagoPlayerClass(1)
        self.enemy = SkeletonMageEnemy(1)
        self.turn_player = TurnPlayer(self.player, self.enemy)


    def test_skill_select_with_no_skills(self):
        self.player.skills = []
        with patch("builtins.print") as mock_print:
            skill = self.turn_player.skill_select()
            mock_print.assert_called_with("Você não tem skills disponíveis")
        self.assertIsNone(skill)


if __name__ == "__main__":
    unittest.main()
