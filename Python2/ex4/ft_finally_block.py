class PlantError(Exception):
    """
    PlantError is a custom error class, which inherits from
    Exception
    """
    def __init__(self, message: str = "Unknown PlantError") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """
    Checks that plant_name is capitalised if it isnt it will raise a
    PlantError
    """
    if not plant_name or plant_name != str.capitalize(plant_name):
        raise PlantError("Caught PlantError: Invalid plant name"
                         f" to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    """
    Tests our function to see if it waters the good and bad plants
    and what errors it throws if there is an issue
    """
    print("=== Garden Watering System ===")
    good_plants = ["Tomatos", "Lettuce", "Carrots"]
    bad_plants = ["Tomatos", "lettuce", "Carrots"]
    both_plants = [good_plants, bad_plants]
    print("\nTesting valid plants...")
    try:
        for plant_list in both_plants:
            print("Opening watering system")
            try:
                for plant in plant_list:
                    water_plant(plant)
            except PlantError as message:
                print(message)
                print(".. ending tests and returning to main")
                return
            finally:
                print("Closing watering system")
            print("\nTesting invalid plants...")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
