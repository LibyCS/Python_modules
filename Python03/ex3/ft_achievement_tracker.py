achievements = {"boss_slayer", "collector", "first_kill", "level_10",
                "perfectionist", "speed_demon", "treasure_hunter"}
alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon",
           "perfectionist"}


def print_sets(set):
    i = 1
    print("{", end="")
    for achievement in set:
        if (i != len(set)):
            print(f"'{achievement}', ", end="")
        else:
            print(f"'{achievement}'}}")
        i += 1


print("=== Achievement Tracker System ===\n")
players = [alice, bob, charlie]
names = ["alice", "bob", "charlie"]
i = 0
for player in players:
    print(f"Player {names[i]} achievements: ", end="")
    print_sets(player)
    i += 1
print("\n=== Achievement Analytics ===")
print("All unique achievements: ", end="")
print_sets(achievements)
print(f"Total unique achievements: {len(achievements)}\n")
print("Common to all players: "
      f"{alice.intersection(bob.intersection(charlie))}")
alice_u = set(alice.difference(bob.union(charlie)))
bob_u = set(bob.difference(alice.union(charlie)))
charlie_u = set(charlie.difference(alice.union(bob)))
print("Rare achievements (1 player): "
      f"{charlie_u.union(alice_u.union(bob_u))}\n")
print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
