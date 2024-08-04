import unittest

from src.PlayerClass import MagoPlayerClass
from src.skills.ABC_skill import TypeSkill


class TestMagoPlayerClass(unittest.TestCase):
    def setUp(self):
        self.magos = [MagoPlayerClass(x) for x in range(1, 6)]

    def test_level_up(self):
        for mago in self.magos:
            level_ant = mago.level
            mago.xp = 100 * level_ant
            if level_ant < 5:
                self.assertEqual(level_ant + 1, mago.level)
            else:
                self.assertEqual(level_ant, mago.level)

    def test_upgrade(self):
        for mago in self.magos:
            self.assertEqual(100 + (mago.level * 10), mago.hpMax)
            self.assertEqual(50 + (mago.level * 10), mago.mpMax)
            self.assertEqual(20 + (mago.level * 5), mago.stMax)

    def test_damage_taken_magico(self):
        damage = 20
        expected_result = 10

        hpAntes = self.magos[0].hpAtual
        self.magos[0].damage_taken(damage, TypeSkill.MAGICO)
        hpDps = self.magos[0].hpAtual

        self.assertEqual(expected_result, hpAntes - hpDps)

    def test_damage_taken_fisico(self):
        damage = 20
        expected_result = 20

        hpAntes = self.magos[0].hpAtual
        self.magos[0].damage_taken(damage, TypeSkill.FISICO)
        hpDps = self.magos[0].hpAtual

        self.assertEqual(expected_result, hpAntes - hpDps)

    def test_skill_cast(self):
        damage, typeSkill = self.magos[0].skill_cast(self.magos[0].skills[0])

        self.assertIn(typeSkill, [TypeSkill.MAGICO, TypeSkill.FISICO])
        self.assertGreaterEqual(damage, 0)


    def test_skill_list_disponivel(self):
        skills_disponiveis = self.magos[0].skill_list_disponivel()
        
        self.assertEqual(2, len(skills_disponiveis))
        self.assertEqual('Fireball', skills_disponiveis[0].name)
        self.assertEqual(1, skills_disponiveis[0].level)


if __name__ == "__main__":
    unittest.main()
