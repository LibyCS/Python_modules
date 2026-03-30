import random


def data_comp() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list = ["Alice", "bob", "Charlie", "dylan",
                     "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Inital list of players: {players}")
    player_cap: list = [name.capitalize() for name in players]
    print(f"New list with all names capitalised: {player_cap}")
    cap_only: list = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalised names only: {cap_only}")
    score_dict: dict[str, int] = {name: random.randrange(1, 1000)
                                  for name in player_cap}
    print(f"\nScore dict: {score_dict}")
    average = round(sum(list(score_dict.values()))/len(score_dict), 2)
    print(f"Score average is {average}")
    high_scores: dict[str, int] = {name: value for name, value in
                                   score_dict.items() if value > average}
    print(f"Hight scores: {high_scores}")


if __name__ == "__main__":
    data_comp()
