from data import pokemon_data, pokemon_attacks
class Pokemon:
    def __init__(self, lvl:int, name:str, current_hp:int, base_stats:dict, stats:dict, attacks:dict, iv:int,
                 ev:int, nature:float):
        self.lvl = lvl
        self.name =name
        self.current_hp = current_hp
        self.base_stats = base_stats
        self.stats = stats
        self.attacks = attacks
        self.iv = iv
        self.ev = ev
        self.nature = nature

    @classmethod
    def create_pokemon(cls, name:str, attacks=None, lvl:int=1, iv:int=0, ev:int=0, 
                       nature:float=1.0)->Pokemon:
        if name not in pokemon_data:
            raise ValueError(f"{name} is incorrect or not implemented yet")
        pok_base_stats = pokemon_data[name]["stats"]
        actual_stats = Pokemon.calculate_stats(pok_base_stats, lvl, iv,ev,nature)
        pok_attacks = {}
        if attacks is None:
            attacks = [pokemon_data[name]["default_attack"]]
        for attack in attacks:
            if attack in pokemon_attacks:
                pok_attacks[attack] = pokemon_attacks[attack]
        pokemon = cls(lvl, name, actual_stats["hp"], pok_base_stats, actual_stats,
                      pok_attacks, iv, ev, nature)
        return pokemon

    @staticmethod
    def calculate_stats(base_stats:dict, lvl:int, iv:int, ev:int, nature)->dict:
        calculated_stats = {}
        for stat in base_stats:
            if stat == "hp":
                calculated_stats[stat] = ((2 * base_stats[stat]  + iv + ev // 4)
                                           * lvl) // 100 + lvl + 10
            else:
                calculated_stats[stat] = int(((((2 * base_stats[stat] + iv + ev // 4)
                                                 * lvl) // 100) + 5) * nature)
        return calculated_stats

    def lvl_up(self)->Pokemon:
        self.lvl += 1
        self.stats = self.calculate_stats(self.base_stats, self.lvl, self.iv, self.ev, self.nature)
        print(
            f"{self.name} leveled up! new stats:\n"
            f"hp = {self.stats["hp"]}\n"
            f"atk = {self.stats["atk"]}\n"
            f"def = {self.stats["defense"]}\n"
            f"spatk = {self.stats["spatk"]}\n"
            f"spdef = {self.stats["spdef"]}\n"
            f"speed = {self.stats["speed"]}"
            )
        return self

    def attack(self, other, attack:str):
        if attack not in self.attacks:
            raise ValueError(f"{attack} is not a valid attack!")
        if self.attacks[attack]["class"] == "physical":
            dmg_dealt  = int((((2 * self.lvl // 5 + 2) * self.attacks[attack]["power"] *
                                self.stats["atk"] // other.stats["defense"]) // 50) + 2)

        elif self.attacks[attack]["class"] == "special":
                    dmg_dealt  = int((((2 * self.lvl // 5 + 2) * self.attacks[attack]["power"] *
                                        self.stats["spatk"] // other.stats["spdef"]) // 50) + 2)
        else:
            raise ValueError("Unknown attack class")
        other.current_hp = max(0, other.current_hp - dmg_dealt)
        print(f"{self.name} uses {attack}!\n"
              f"{other.name} recieves {dmg_dealt} damage!"
              )

    def is_fainted(self)->bool:
        if self.current_hp == 0:
            return True
        return False


        
            



        


   
