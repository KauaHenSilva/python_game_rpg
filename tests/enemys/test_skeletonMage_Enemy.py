from typing import List
import unittest

from src.Class import SkeletonMageClass
from src.skills.ABC_skill import TypeSkill


class TestSkeletonMageEnemy(unittest.TestCase):
    def setUp(self):
        self.enemys: List[SkeletonMageClass] = [SkeletonMageClass(x) for x in range(1, 6)]

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
            self.assertEqual(100 + (enemy.level * 10) + (enemy.level * 2), enemy.hpMax)
            self.assertEqual(50 + (enemy.level * 10), enemy.mpMax)
            self.assertEqual(20 + (enemy.level * 5), enemy.stMax)
    
    def test_skill(self):
        for enemy in self.enemys:
            self.assertEqual(2, len(enemy.skills))
            self.assertEqual('Bola de fogo', enemy.skills[0].name)
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
