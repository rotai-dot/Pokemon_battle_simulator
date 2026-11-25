# Pokémon Battle Simulator

A small command-line Pokémon battle simulator built in Python as a learning project alongside the Boot.dev course.

**Status: Alpha — v0.1.0**

The current version provides a complete, simplified battle: choose your Pokémon, select a move and level, and watch the battle until a winner is declared.

## Requirements

- Python 3.14 or later.
- No external dependencies.

## Getting started

Clone the repository and enter the project directory:

```bash
git clone https://github.com/rotai-dot/Pokemon_battle_simulator.git
cd Pokemon_battle_simulator
```

Run the simulator:

```bash
python3 main.py
```

Follow the prompts to choose:

1. A Pokémon: Pikachu or Charmander.
2. A move: Thundershock or Tackle.
3. A level between 1 and 100.

Your opponent is a Charmander at the same level, using Tackle. Both Pokémon repeat their selected moves until one faints.

Invalid Pokémon names, move names and level inputs prompt you to try again.

## Implemented features

- Pokémon creation and level-based stat calculation.
- Physical and special damage calculation.
- Turn order determined by Speed.
- Random turn order when Speed is tied.
- HP tracking, with a minimum of zero.
- Fainting checks that prevent a defeated Pokémon from attacking.
- Automatic battles and winner announcements.
- Console input validation.
- Unit tests for Pokémon creation, leveling and battle behavior.

## Project structure

```text
Pokemon_battle_simulator/
├── main.py               # Console interaction and battle loop
├── pokemon.py            # Pokémon creation, stats and damage
├── battle.py             # Turn order and turn execution
├── data.py               # Pokémon and move definitions
├── tests/
│   ├── test_pokemon.py
│   └── test_battle.py
├── test.sh               # Test runner for Bash
└── README.md
```

## Running tests

From the project directory:

```bash
python3 -m unittest discover -s tests -v -b
```

Alternatively, in Bash:

```bash
bash test.sh
```

## Current limitations

This alpha intentionally keeps the mechanics simple:

- Only two Pokémon and two moves are available.
- The opponent is always Charmander.
- Any available move can be assigned to either Pokémon.
- One move is selected before battle and repeated automatically.
- Move types are stored, but type effectiveness and STAB are not applied.
- Accuracy, critical hits, PP, status conditions and damage randomness are not implemented.
- IV, EV and nature parameters exist in the code but cannot be configured through the console. The console uses their default values.
- The simulator does not reproduce all official Pokémon battle rules.

## Learning goals

This project practices:

- Classes, instance methods, class methods and static methods.
- Dictionaries and nested data structures.
- Imports and separation into modules.
- Loops, conditions and console input.
- Exceptions and input validation.
- Unit testing with Python's `unittest` module.

The alpha is a deliberately limited milestone for the backend depeloper course on boot.dev. Further features may or may not be added as the course progresses.

## Disclaimer

This is an unofficial educational fan project, unaffiliated with Nintendo, Game Freak or The Pokémon Company.