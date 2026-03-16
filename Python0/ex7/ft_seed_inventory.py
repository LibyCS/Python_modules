def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "area" or unit == "grams" or unit == "packets":
        print((seed_type.capitalize()) + " seeds: ", end="")
        if unit == "grams":
            print(quantity, unit, end="")
            print(" total")
        elif unit == "area":
            print("covers", quantity, "square meters")
        else:
            print(quantity, unit, end="")
            print(" available")
    else:
        print("Unknown unit type")
