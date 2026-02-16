def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print((seed_type.capitalize()) + " seeds: ", end="")
    if unit != "area":
        print(quantity, unit, end="")
        if unit == "grams":
            print(" total")
        else:
            print(" available")
    else:
        print("covers", quantity, "square meters")
