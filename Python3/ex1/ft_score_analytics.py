import sys


def analytics() -> None:
    """
    gives statistics based on the given scores
    inputed
    """
    print("=== Player Score Analytics ===")
    args = sys.argv
    score_list: list = []
    i = 1
    while i < len(args):
        try:
            score_list = score_list + [int(args[i])]
        except ValueError:
            print(f"Invalid parameter: \'{args[i]}\'")
        i += 1
    if len(args) == 1 or not score_list:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...\n")
        return
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {(sum(score_list)/len(score_list)):.1f}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")
    print()


if __name__ == "__main__":
    analytics()
