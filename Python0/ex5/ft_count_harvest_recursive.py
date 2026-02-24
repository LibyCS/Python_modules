def ft_count_harvest_recursive() -> None:
    num_days = int(input("Days until harvest: "))

    def recursive_days(day) -> None:
        if day != 1:
            recursive_days(day - 1)
        print("Day", day)
    recursive_days(num_days)
    print("Harvest time!")
