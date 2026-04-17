from ex0 import Creature, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy
from ex2 import NormalStrategy, DefensiveStrategy, AgressiveStrategy


def format(participants: list[tuple[Creature, BattleStrategy]]) -> None:
    """
    print the participants and strategy like in the example
    """
    index = 0
    print("[ ", end="")
    for creature, strat in participants:
        print(f"({creature.name}+{strat.name})", end="")
        if index != len(participants) - 1:
            print(", ", end="")
        index += 1
    print(" ]")


def battle(participants: list[tuple[Creature, BattleStrategy]]) -> None:
    """
    With the list given it makes sure all the opponents
    fight each other and carry out the strategy if they are valid
    for the creature
    """
    i: int = 0
    if len(participants) <= 1:
        print("Error: Not enough participants")
    print("*** Tournament ***")
    print(f"{len(participants)} opponents involved")
    for fighter, fstrategy in participants:
        i += 1
        if i == len(participants):
            break
        for opponent, ostrategy in participants[i:]:
            print("\n* Battle *")
            print(f"{fighter.describe()}\n vs.\n{opponent.describe()}")
            print(" now fight!")
            try:
                fstrategy.act(fighter)
                ostrategy.act(opponent)
            except AttributeError as message:
                print(message)


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()
    norm = NormalStrategy()
    agg = AgressiveStrategy()
    defe = DefensiveStrategy()
    i: int = 0
    while i < 3:
        print(f"\nTournament {i} ", end="")
        if i == 0:
            print("(basic)")
            fighters = [(flame.create_base(), norm), (heal.create_base(),
                                                      defe)]
        elif i == 1:
            print("(error)")
            fighters = [(flame.create_base(), agg), (heal.create_base(),
                                                     defe)]
        elif i == 2:
            print("(multiple)")
            fighters = [(aqua.create_base(), norm), (heal.create_base(), defe),
                        (trans.create_base(), agg)]
        format(fighters)
        battle(fighters)
        i += 1
