import sys


def get_args() -> dict[str, int]:
    """
    gets the args from input and sticks them
     in a dictionary
    """
    args = sys.argv
    inventory: dict[str, int] = {}
    for arg in args[1:]:
        i = 0
        if ":" not in arg:
            print(f"Error - invalid parameter \'{arg}'")
            continue
        for c in arg:
            if c == ":" and arg[:i] not in inventory:
                try:
                    inventory[arg[:i]] = int(arg[i + 1:])
                except ValueError:
                    print(f"Quantity error for \'{arg[:i]}\'"
                          ": invalid literal for int() with "
                          f"base 10: \'{arg[i + 1:]}\'")
            elif arg[:i] in inventory:
                print(f"Redundant item \'{arg[:i]}\' - discarding")
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
    total: int = 0
    for i in diction.values():
        total += i
    return total


def init_dict(diction) -> dict[str, dict[str, int]]:
    """
    initialises the stat dictionary which has
    nested dictionaries as it values
    """
    stats: dict[str, dict[str, int]] = {}
    most = None
    least = None
    for item in diction:
        if most == None or diction[item] > most:
            stats["most"] = {item: diction[item]}
            most = diction[item]
        if least == None or diction[item] < least:
            stats["least"] = {item: diction[item]}
            least = diction[item]
    return stats


def system() -> None:
    """
    formats it to print like the example
    given
    """
    inventory: dict[str, int] = get_args()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory.keys())}"
          f" items: {sum(inventory.values())}")
    for item in inventory:
        percentage = (inventory[item] / sum(inventory.values())) * 100
        print(f"Item {item} represents {percentage:.1f}%")
    stats = init_dict(inventory)
    if "most" in stats:
        for item in stats["most"]:
            print(f"Item most abundant: {item} "
                  f"with quantity {inventory.get(item)}")
    if "least" in stats:
        for item in stats["least"]:
            print(f"Item least abundant: {item} "
                  f"with quantity {inventory.get(item)}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    system()
