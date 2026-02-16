def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Determines what Errors it shoudl raise if there is one
    depending on weather plant_name is empty,and that the water level
    and sunlight hours are acceptable
    :param plant_name: name of plant
    :param water_level: water level of tank
    :param sunlight_hours: how many hours the plant has been exposed
    to sunlight
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Error: Water level {water_level}"
                             " is too low (min 1)")
        else:
            raise ValueError(f"Error: Water level {water_level}"
                             " is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")
    return "Plant '" + plant_name + "' is healthy!"


def test_plant_checks():
    """
    tests the errors that are raised based on plant name,
    water levels and sunlight hours
    """
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        print(check_plant_health("Tomato", 2, 10))
    except ValueError as message:
        print(message)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 3, 5)
    except ValueError as message:
        print(message)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Lettuce", 0, 10)
    except ValueError as message:
        print(message)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Lettuce", 12, 10)
    except ValueError as message:
        print(message)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Carrots", 3, 0)
    except ValueError as message:
        print(message)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Carrots", 3, 15)
    except ValueError as message:
        print(message)
    print("\nAll error raising tests completed!")


test_plant_checks()
