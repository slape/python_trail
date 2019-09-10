import unittest
from src.models import Player


class TestModels(unittest.TestCase):

    def test_player_factory(self):
        number = 1
        name = 'Miss Garbanzo'
        trail_options = ['Active Volcano to the Left',
                         'Inactive Void of Once-Active Volcano to the Right']
        supplies = ['Vicodin', 'Revolver', 'Single Bullet', 'Garlic']
        calamities = ['Yellowstone explodes', 'Your gallstones explode']

        p: Player = Player.create(
            number, name, supplies, trail_options, calamities)

        self.assertEqual(number, p.number)
        self.assertEqual(name, p.name)
        for trail, supply in zip(trail_options, supplies):
            self.assertEqual(1, p.trail_options.get(trail))
            self.assertEqual(1, p.supplies.get(supply))

    def test_gain_supply(self):
        self.fail()

    def test_lose_supply(self):
        self.fail()

    def test_trail_hash(self):
        self.fail()


if __name__ == "__main__":
    unittest.main()
