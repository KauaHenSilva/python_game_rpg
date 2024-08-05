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
            for _ in range(10):
                self.fire_skill.skill_cast()

    def test_setStats(self):
        self.fire_skill.setStats()
        self.assertEqual(15, self.fire_skill.costMP)
        self.assertEqual(10, self.fire_skill.damage)

    def test_skill_cast(self):
        damage, typeSkill = self.fire_skill.skill_cast()
        self.assertEqual(10, damage)
        self.assertEqual(TypeSkill.MAGICO, typeSkill)
        self.assertEqual(1, self.fire_skill.level)
        self.assertEqual(15, self.fire_skill.costMP)
        self.assertEqual(0, self.fire_skill.costST)


if __name__ == "__main__":
    unittest.main()
