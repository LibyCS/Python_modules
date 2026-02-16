class GardenError(Exception):
    """
    GardenError is the parent class Error for both WaterError and PlantError
    takes the properties of Exception
    """
    pass


class WaterError(GardenError):
    """
    WaterError is the child class Error of GardenError and inherits its
    properties
    """
    pass


class PlantError(GardenError):
    """
    PlantError is the child class Error of GardenError and inherits its
    properties
    """
    pass


def garden_check(plant, water):
    """
    Garden check takes in the age of the plant and the amount of days it was
    last watered. Then raises the appropriate Errors depending on each
    value.
    :param plant: number of days its been growing
    :param water: number of days since last watered
    """
    if plant > 70 and water < 10:
        raise GardenError
    elif plant > 70:
        raise PlantError
    elif water < 10:
        raise WaterError


def test():
    """
    Test tests each value and see how it raises specific custom errors
    depending on the parameters given
    """
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        garden_check(71, 11)
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!")
    print("\nTesting WaterError...")
    try:
        garden_check(61, 9)
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!")
    print("\nTesting catching all garden errors..")
    try:
        garden_check(71, 9)
    except GardenError:
        print("Caught a garden error: The tomato plant is wilting!")
        print("Caught a garden error: Not enough water in the tank!")
    print("\nAll custom error types work correctly!")


test()
