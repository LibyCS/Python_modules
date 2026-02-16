import sys

print("=== Player Score Analytics ===")
args = sys.argv
score_list = []
i = 1
while i < len(args):
    try:
        score_list = score_list + [int(args[i])]
    except ValueError:
        print(f"Unfortunately {args[i]} is not an int")
    i += 1
if len(args) == 1:
    print("No valid scores have been entered")
else:
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(args) - 1}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list)/len(args)}")
    print(f"Highest score: {max(score_list)}")
    print(f"Lowest score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}")

