from battle import Battle
from pokemon import Pokemon
from data import pokemon_data, pokemon_attacks

def main():
    print("Welcome to a very bad and still not even too much playable pokemon simulator!")
    print("In this simulator you can choose the pokemon name, it's attacks, lvl, ivs, evs and nature (not implemented yet)")
    print("choose your pokemon option behind:")
    for pokemon in pokemon_data:
        print(f"{pokemon}")
    while True:
        pokemon1_name = input("your choose, pokemon master: ").strip().lower()
        if pokemon1_name in pokemon_data:
            break
        else:
            print(f"{pokemon1_name} is not a valid pokemon, trainer, choose again")
    print("now you will choose the pokemon attack to be played until a pokemon is killed")
    for move in pokemon_attacks:
        print(move)
    while True:
        pokemon_attack = input("your attack choice master: ").strip().lower()
        if pokemon_attack in pokemon_attacks:
            break
        else:
            print(f"{pokemon_attack} is not a valid move, trainer, choose again")
    while True:
        try:
            lvl = int(input("Choose the combatant lvl: "))
        except ValueError:
            print("A whole number is needed")
            continue

        if 1 <= lvl <= 100:
            break

        print("Your pokemon level must be between 1 and 100. Have you ever played pokemon?")
            
    
        
    pokemon1 = Pokemon.create_pokemon(name = pokemon1_name, attacks=[pokemon_attack],
                                      lvl=lvl)
    charmander = Pokemon.create_pokemon("charmander", lvl=lvl)
    battle1 = Battle(pokemon1, charmander)
    while not pokemon1.is_fainted() and not charmander.is_fainted():
        battle1.turn(pokemon_attack, "tackle")

    if pokemon1.is_fainted():
        print(f"{charmander.name} won the battle!")
    else:
        print(f"{pokemon1.name} won the battle!")






if __name__ == "__main__":
    main()