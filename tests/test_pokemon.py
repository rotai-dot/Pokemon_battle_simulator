import unittest
from pokemon import Pokemon
import io
from contextlib import redirect_stdout

class TestPokemon(unittest.TestCase):

    def test_create_pokemon(self):
        pikachu = Pokemon.create_pokemon("pikachu", lvl=5)

        self.assertEqual(pikachu.name, "pikachu")
        self.assertEqual(pikachu.lvl, 5)
        self.assertIn("thundershock", pikachu.attacks)

    def test_invalid_pokemon(self):
        with self.assertRaises(ValueError):
            Pokemon.create_pokemon("Harry Potter")

    def test_level_up(self):
        pikachu = Pokemon.create_pokemon("pikachu", lvl=5)
        output = io.StringIO()
        pikachu.lvl_up()   
        self.assertEqual(pikachu.lvl, 6)

    def test_calculate_stats_in_lvl_up(self):
        pikachu = Pokemon.create_pokemon("pikachu", lvl=5)
        pikachu_lvl_6 = Pokemon.create_pokemon("pikachu", lvl=6)
        pikachu.lvl_up()
        output = io.StringIO()
        self.assertEqual(pikachu.stats, pikachu_lvl_6.stats)


    


if __name__ == "__main__":
    unittest.main()