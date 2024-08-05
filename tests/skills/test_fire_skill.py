import unittest
from src.skills.fire_skill import FireSkill, TypeSkill


class TestFireSkill(unittest.TestCase):
    def setUp(self):
        self.fire_skill = FireSkill()

    def test_action(self):
        expected_output = "Fireball"
        self.assertEqual(expected_output, self.fire_skill.action())

    def test_upgrade_cast(self):
        for x in range(1, 6):
            self.assertEqual(x, self.fire_skill.level)
            for _ in range(10 * self.fire_skill.level):
                self.fire_skill.skill_cast()

    def test_setStats(self):
        self.fire_skill.setStats()
        self.assertEqual(5, self.fire_skill.costMP)
        self.assertEqual(12, self.fire_skill.damage)

    def test_skill_cast(self):
        mpAtual = 10
        stAtual = 10

        damage, typeSkill = self.fire_skill.skill_cast()
        self.assertEqual(12, damage)
        self.assertEqual(TypeSkill.MAGICO, typeSkill)
        self.assertEqual(1, self.fire_skill.level)
        self.assertEqual(5, mpAtual - self.fire_skill.costMP)
        self.assertEqual(10, stAtual - self.fire_skill.costST)


if __name__ == "__main__":
    unittest.main()
