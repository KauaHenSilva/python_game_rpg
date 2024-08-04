import unittest

from src.enemysClass import SkeletonMageEnemyClass
from src.skills.ABC_skill import TypeSkill


class TestSkeletonMageEnemy(unittest.TestCase):
    def setUp(self):
        self.enemys = [SkeletonMageEnemyClass(x) for x in range(1, 6)]

    def test_damage_taken_magico(self):
        damage = 20
        expected_result = 10

        hp_antigo = self.enemys[0].hpAtual
        self.enemys[0].damage_taken(damage, TypeSkill.MAGICO)
        hp_novo = self.enemys[0].hpAtual

        self.assertEqual(expected_result, hp_antigo - hp_novo)

    def test_damage_taken_fisico(self):
        damage = 20
        expected_result = 20

        hp_antigo = self.enemys[0].hpAtual
        self.enemys[0].damage_taken(damage, TypeSkill.FISICO)
        hp_novo = self.enemys[0].hpAtual

        self.assertEqual(expected_result, hp_antigo - hp_novo)

    def test_setStats(self):
        for enemy in self.enemys:
            self.assertEqual(50 + (enemy.level * 10), enemy.hpMax)
            self.assertEqual(10 + (enemy.level * 5), enemy.mpMax)
            self.assertEqual(10 + (enemy.level * 5), enemy.stMax)
            self.assertEqual(enemy.level * 100, enemy.xp)
    
    def test_skill(self):
        for enemy in self.enemys:
            self.assertEqual(1, len(enemy.skills))
            self.assertEqual('Fireball', enemy.skills[0].name)
            self.assertIn(enemy.skills[0].level, range(1, enemy.level + 1))
            
    def test_skill_return(self):
        for enemy in self.enemys:
            for skill in enemy.skills:
                valor, typeSkill = enemy.skill_cast(skill)
                if typeSkill is not None:
                    self.assertIn(typeSkill, [TypeSkill.MAGICO, TypeSkill.FISICO])
                    self.assertGreaterEqual(valor, 0)
                else:
                    self.assertEqual(0, valor)
                    self.assertIsNone(typeSkill)
                

    def test_skill_cast(self):
        for enemy in self.enemys:
            for skill in enemy.skills:
                valor, typeSkill = enemy.skill_cast(skill)
                if typeSkill is not None:
                    self.assertIn(typeSkill, [TypeSkill.MAGICO, TypeSkill.FISICO])
                    self.assertGreaterEqual(valor, 0)
                else:
                    self.assertEqual(0, valor)
                    self.assertIsNone(typeSkill)
        
        with self.assertRaises(ValueError):
            enemy.skill_cast(None)
            
        for enemy in self.enemys:
            enemy.mpAtual = 0
            for skill in enemy.skills:
                valor, typeSkill = enemy.skill_cast(skill)
                self.assertEqual(0, valor)
                self.assertIsNone(typeSkill)
            
            

        
    def test_skill_damage(self):
        for enemy in self.enemys:
            enemy.mpAtual = 100
            enemy.stAtual = 100
            for skill in enemy.skills:
                valor, typeSkill = enemy.skill_cast(skill)
                if typeSkill == TypeSkill.MAGICO:
                    self.assertEqual(int(valor), valor)
                else:
                    self.assertEqual(int(valor * 0.5), valor)
        

if __name__ == "__main__":
    unittest.main()
