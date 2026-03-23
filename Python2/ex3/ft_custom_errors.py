class GardenError(Exception):
    """
    GardenError is the parent class Error for both WaterError and PlantError
    takes the properties of Exception
    """
    default_message = "Unknown GardenError"
    def __init__(self, message: str) -> None:
        super().__init__(message or self.default_message)


class WaterError(GardenError):
    """
    WaterError is the child class Error of GardenError and inherits its
    properties
    """
    default_message = "Unknown WaterError"


class PlantError(GardenError):
    """
    PlantError is the child class Error of GardenError and inherits its
    properties
    """
    default_message = "Unknown PlantError"


def garden_check(plant: int, water: int) -> None:
    """
    Garden check takes in the age of the plant and the amount of days it was
    last watered. Then raises the appropriate Errors depending on each
    value.
    :param plant: number of days its been growing
    :param water: number of days since last watered
    """
    if plant > 70 and water < 10:
        raise GardenError("Caught a GardenError: The tomato plant is wilting!"
                          "\nCaught a GardenError: Not enough water in the tank!")
    elif plant > 70:
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    elif water < 10:
        raise WaterError("Caught WaterError: Not enough water in the tank!")


def test_errors() -> None:
    """
    Test tests each value and see how it raises specific custom errors
    depending on the parameters given
    """
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        garden_check(71, 11)
    except PlantError as message:
        print(message)
    print("\nTesting WaterError...")
    try:
        garden_check(61, 9)
    except WaterError as message:
        print(message)
    print("\nTesting catching all garden errors..")
    try:
        garden_check(71, 9)
    except GardenError as message:
        print(message)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
