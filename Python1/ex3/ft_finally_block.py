def water_plants(plant_list):
    """
    Goes through the plant list and waters each plant unless
    an error is raised
    :param plant_list: a list of all plants in the system
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed successfully!")
    except TypeError:
        print("Error: Cannot water", plant, "- invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Tests our function to see if it waters the good and bad plants
    and what errors it throws if there is an issue
    """
    print("=== Garden Watering System ===")
    good_plants = ["Tomatos", "Lettuce", "Carrots"]
    bad_plants = ["Tomatos", None, "Carrots"]
    print("\nTesting normal watering...")
    try:
        water_plants(good_plants)
        print("\nTesting with error...")
        water_plants(bad_plants)
    finally:
        print("\nCleanup always happens, even with errors!")


test_watering_system()
