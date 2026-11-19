import unittest
from battle import Battle
from pokemon import Pokemon
import io
from contextlib import redirect_stdout


class TestBattle(unittest.TestCase):
    def test_turn(self):
        pikachu = Pokemon.create_pokemon(name="pikachu", lvl=5)
        charmander = Pokemon.create_pokemon(name="charmander", lvl=5)
        state = Battle(pikachu,charmander)
        turn_result =state.turn("thundershock", "tackle")
        output = io.StringIO()
        self.assertEqual(pikachu.current_hp, 12)
        self.assertEqual(charmander.current_hp, 13)
        self.assertTrue(turn_result)
        self.assertFalse(pikachu.is_fainted())
        self.assertFalse(charmander.is_fainted())
    
    def test_reverse_turn_order(self):
        pikachu = Pokemon.create_pokemon("pikachu", lvl=5)
        charmander = Pokemon.create_pokemon("charmander", lvl=5)

        charmander.stats["speed"] = pikachu.stats["speed"] + 1
        battle = Battle(pikachu, charmander)

        output = io.StringIO()
        with redirect_stdout(output):
            result = battle.turn("thundershock", "tackle")

        self.assertTrue(result)
        self.assertEqual(output.getvalue().splitlines()[0],
                        "charmander used tackle")


    def test_first_attack_ko(self):
        pikachu = Pokemon.create_pokemon("pikachu", lvl=5)
        charmander = Pokemon.create_pokemon("charmander", lvl=5)

        charmander.current_hp = 1
        initial_hp = pikachu.current_hp

        battle = Battle(pikachu, charmander)

        with redirect_stdout(io.StringIO()):
            result = battle.turn("thundershock", "tackle")

        self.assertFalse(result)
        self.assertEqual(charmander.current_hp, 0)
        self.assertEqual(pikachu.current_hp, initial_hp)

    def test_invalid_attack(self):
        pikachu = Pokemon.create_pokemon("pikachu", lvl=5)
        charmander = Pokemon.create_pokemon("charmander", lvl=5)

        battle = Battle(pikachu, charmander)

        initial_hp1 = pikachu.current_hp
        initial_hp2 = charmander.current_hp

        with self.assertRaises(ValueError):
            battle.turn("thundershock", "flamethrower")

        self.assertEqual(pikachu.current_hp, initial_hp1)
        self.assertEqual(charmander.current_hp, initial_hp2)