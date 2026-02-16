class GardenError(Exception):
    """
    GardenError is the parent class Error for both WaterError and PlantError
    takes the properties of Exception
    """
    pass


class GardenNameError(GardenError):
    """
    GardenNameError is the child class Error of GardenError and inherits its
    properties
    """
    pass


class WaterError(GardenError):
    """
    WaterError is the child class Error of GardenError and inherits its
    properties
    """
    pass


class SunError(GardenError):
    """
    SunError is the child class Error of GardenError and inherits its
    properties
    """
    pass


class GardenManager:
    """
    The main class which stores information about the plants that have
    been added, also contains the methods that can act on the plants
    in the list it has stored
    """

    def __init__(self):
        """
        gives the class a variable list that can be accessed across its
        methods. Stores all the plant names water and sunlight hours
        :param self: Description
        """
        self.plants = []

    def add_plant(self, vegetable, water, sun):
        """
        Adds specified plant listed as vegetable in the params its
        water level and sunlight hours into a tuple and then added to
        the plants list.
        :param self: self
        :param vegetable: plant name
        :param water: water levels
        :param sun: sunlight hours
        """
        if not vegetable:
            raise GardenNameError
        self.plants = self.plants + [(vegetable, water, sun)]
        print("Added", vegetable, "successfully")

    def water_plant(self):
        """
        waters all the plants, no errors to raise as the plant names
        should have all been checked earlier
        """
        print("Opening watering system")
        for plant in self.plants:
            print("Watering", plant, "- success")

    def plant_health(self, plant, water, sun):
        """
        checks the plant health depending on the water and sunlight levels
        and raises errors if their values arent in an acceptable range
        params plant: plant name
        params water: water level
        params sun: sunlight hours
        """
        if not 1 <= water <= 10 and not 2 <= sun <= 12:
            raise GardenError("Caught GardenError: Not enough water in tank")
        elif water < 1:
            raise WaterError(f"Error checking {plant}: "
                             f"Water level {water} is too low (min 1)")
        elif water > 10:
            raise WaterError(f"Error checking {plant}: "
                             f"Water level {water} is too high (max 10)")
        elif sun < 2:
            raise SunError(f"Error checking {plant}: "
                           f"Sunlight hours {sun} is too low (min 2)")
        elif sun > 12:
            raise SunError(f"Error checking {plant}: "
                           f"Sunlight hours {sun} is too high (max 12)")
        print(f"{plant} is healthy (water: {water} sun: {sun})")


def testing():
    """
    Testing tests each method in the gardanmanger with various
    plants and water levels and sunlight hours, it tests how i handle
    the errors which may arise.
    garden is the class instance with the gardenmanager class properties
    """
    print("=== Garden Management System ===")
    garden = GardenManager()
    try:
        print("\nAdding plants to garden...")
        garden.add_plant("Tomato", 2, 4)
        garden.add_plant("Lettuce", 1, 10)
        garden.add_plant("Carrot", 2, 15)
        garden.add_plant("", 5, 6)
    except GardenNameError:
        print("Error adding plant: Plant name cannot be empty!")
    try:
        print("\nWatering plants...")
        garden.water_plant()
    finally:
        print("Closing watering system (cleanup)")
    try:
        print("\nChecking plant health...")
        garden.plant_health("Tomato", 2, 4)
        garden.plant_health("Lettuce", 1, 10)
        garden.plant_health("Carrot", 15, 10)
    except (GardenError, WaterError, SunError) as message:
        print(message)
    try:
        print("\nTesting error recovery...")
        garden.plant_health("Cucumber", 0, 20)
    except (GardenError, WaterError, SunError) as message:
        print(message)
        print("System recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


testing()
