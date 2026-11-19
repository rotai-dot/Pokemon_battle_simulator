from pokemon import Pokemon
import random

class Battle:
    def __init__(self, pokemon1:Pokemon, pokemon2:Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def turn_order(self)->tuple[Pokemon,Pokemon]:
        if self.pokemon1.stats["speed"]>self.pokemon2.stats["speed"]:
            return (self.pokemon1,self.pokemon2)
        elif self.pokemon2.stats["speed"]>self.pokemon1.stats["speed"]:
            return (self.pokemon2,self.pokemon1)
        else:
            random_int = random.randint(0, 1)
            if random_int == 0:
                return (self.pokemon1,self.pokemon2)
            else:
                return (self.pokemon2,self.pokemon1)
            
    def turn(self, pok1_attack:str, pok2_attack:str)->bool:
        if self.pokemon1.is_fainted() or self.pokemon2.is_fainted():
            raise RuntimeError("Can`t use turn() with a fainted pokemon")
        
        if pok1_attack not in self.pokemon1.attacks:
            raise ValueError(f"{pok1_attack} is not a valid attack for {self.pokemon1.name}")
        
        if pok2_attack not in self.pokemon2.attacks:
                    raise ValueError(f"{pok2_attack} is not a valid attack for {self.pokemon2.name}")

        first, second = self.turn_order()

        for attacker, defender in ((first, second),(second, first)):
            if attacker is self.pokemon1:
                attack_used = pok1_attack
            else:
                attack_used = pok2_attack
            damage = attacker.calculate_damage(defender, attack_used)
            print(f"{attacker.name} used {attack_used}")
            defender.receive_damage(damage)
            print(f"{defender.name} recieved {damage} damage!")

            if defender.is_fainted():
                print(f"{defender.name} fainted!")
                return False

        return True
        
            

