def test_error_types():
    """
    Tests each function in garden_operations with fails safes in place for
    the inevitable crashes due to different Error types.
    This function catches and prints the apropriate message for each Error
    """
    value_error, zero_error, file_error, key_error, multi = garden_operations()
    try:
        value_error()
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        zero_error()
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        file_error()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        key_error()
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    try:
        multi()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        print("\nAll error types tested successfully!")


def garden_operations():
    """
    Defines all the functions that will be used to test each type of errors
    there are.
    Returns: All the functions
    """
    plant = {"Rose": 2}
    print("=== Garden Error Types Demo ===")

    def value_error():
        print("\nTesting ValueError...")
        int("abc")

    def zero_error():
        print("\nTesting ZeroDivisionError...")
        12 / 0

    def file_error():
        print("\nTesting FileNotFoundError...")
        open("missing.txt", "r")

    def key_error():
        print("\nTesting KeyError...")
        plant["Tulips"]

    def multi():
        print("\nTesting multiple errors together...")
        int("abc") / 0
    return value_error, zero_error, file_error, key_error, multi


test_error_types()
