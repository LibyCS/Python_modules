import random


class All():
    achievements = {"Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"}


def gen_player_achievements() -> set:
    player: set = set()
    amount = random.randrange(3, len(All.achievements))
    while amount != 0:
        pending = random.choice(list(All.achievements))
        if pending not in player:
            player.add(pending)
            amount -= 1
    return player


def print_set(set) -> None:
    i = 1
    if not set:
        print("set()")
        return
    print("{", end="")
    for achievement in set:
        if (i != len(set)):
            print(f"'{achievement}', ", end="")
        else:
            print(f"'{achievement}'}}")
        i += 1


def tracker():
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    players = [alice, bob, charlie, dylan]
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    i = 0
    common = set()
    for player in players:
        print(f"Player {names[i]}: ", end="")
        print_set(player)
        if i != 0:
            common = player.intersection(common)
        else:
            common = player
        i += 1
    print("\nAll distinct achievements: ", end="")
    print_set(All.achievements)
    print("\nCommon achievements: ", end="")
    print_set(common)
    print()
    for player, name in zip(players, names):
        all_others = set()
        for other in players:
            if player == other:
                continue
            if not all_others:
                all_others = other
            else:
                all_others = other.union(all_others)
        print(f"Only {name} has: {player.difference(all_others)}")
    print()
    for player, name in zip(players, names):
        print(f"{name} is missing: {All.achievements.difference(player)}")


if __name__ == "__main__":
    tracker()
