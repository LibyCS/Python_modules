import sys

args = sys.argv

inventory = {}
for arg in args:
    i = 0
    for c in arg:
        if c == ":":
            inventory[arg[:i]] = int(arg[i + 1:])
        i += 1


def print_items(diction) -> None:
    first = True
    for item in diction:
        if first == True:
            print(f"{item}", end="")
            first = False
        else:
            print(f", {item}", end="")
    print("")


def total_items(diction) -> int:
    total = 0
    for i in diction.values():
        total += i
    return total


def init_dict(diction) -> dict[str, dict[str, int]]:
    stats = {}
    most = 0
    least = 0
    stats["moderate"] = {}
    stats["scarce"] = {}
    stats["restock"] = {}
    for item in diction:
        if diction[item] > most or most == 0:
            stats["most"] = {item: diction[item]}
            most = diction[item]
        if diction[item] < least or least == 0:
            stats["least"] = {item: diction[item]}
            least = diction[item]
        if diction[item] >= 5:
            stats["moderate"].update({item: diction[item]})
        else:
            stats["scarce"].update({item: diction[item]})
        if diction[item] == 1:
            stats["restock"].update({item: diction[item]})
    return stats


total = total_items(inventory)
print("=== Inventory System Analysis ==")
print(f"Total items in inventory: {total_items(inventory)}")
print(f"Unique item types: {len(inventory.keys())}")
print("\n=== Current Inventory ===")
for item in inventory:
    percentage = (inventory[item] / total) * 100
    print(f"{item}: {inventory[item]} units "
          f"({percentage:.1f}%)")
print("\n=== Inventory Statistics ===")
stats = init_dict(inventory)
for item in stats["most"]:
    print(f"Most abundant: {item} ({inventory.get(item)} units)")
for item in stats["least"]:
    print(f"Least abundant: {item} ({inventory.get(item)} units)")
print("\n=== Item Categories ===")
print(f"Moderate: {stats['moderate']}")
print(f"Scarce: {stats['scarce']}")
print("\n=== Management Suggestions ===")
print(f"Restock needed: ", end="")
print_items(stats["restock"].keys())
print("\n=== Dictionary Properties Demo ===")
print(f"Dictionary keys: ", end="")
print_items(inventory.keys())
print(f"Dictionary values: ", end="")
print_items(inventory.values())
if inventory.get("sword") != None:
    print("Sample lookup - 'sword' in inventory: True")
else:
    print("Sample lookup - 'sword' in inventory: False")
