import sys


def get_args() -> dict[str, int]:
    """
    gets the args from input and sticks them
     in a dictionary
    """
    args = sys.argv
    inventory = {}
    for arg in args:
        i = 0
        for c in arg:
            if c == ":":
                inventory[arg[:i]] = int(arg[i + 1:])
            i += 1
    return inventory


def print_items(diction) -> None:
    """
    recieves a dict values/keys and
    prints out all of them in a formatted
    way
    """
    first = True
    for item in diction:
        if first is True:
            print(f"{item}", end="")
            first = False
        else:
            print(f", {item}", end="")
    print("")


def total_items(diction) -> int:
    """
    adds up all the values and returns it
    """
    total = 0
    for i in diction.values():
        total += i
    return total


def init_dict(diction) -> dict[str, dict[str, int]]:
    """
    initialises the stat dictionary which has
    nested dictionaries as it values
    """
    stats = {}
    most = 0
    least = 0
    stats["most"] = {}
    stats["least"] = {}
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


def demo() -> None:
    """
    formats it to print like the example
    given
    """
    inventory = get_args()
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
    print("Restock needed: ", end="")
    print_items(stats["restock"].keys())
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    print_items(inventory.keys())
    print("Dictionary values: ", end="")
    print_items(inventory.values())
    if inventory.get("sword") is not None:
        print("Sample lookup - 'sword' in inventory: True")
    else:
        print("Sample lookup - 'sword' in inventory: False")


demo()
