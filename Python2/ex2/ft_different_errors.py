def test_error_types() -> None:
    """
    Tests each function in garden_operations with fails safes in place for
    the inevitable crashes due to different Error types.
    This function catches and prints the apropriate message for each Error
    """
    value_error, zero_error, file_error, type_error, mult = garden_operations()
    print("=== Garden Error Types Demo ===")
    try:
        print("Testing operation 0...")
        value_error()
    except ValueError:
        print("Caught ValueError: invalid literal for int() "
              "with base 10: \'abc\'")
    try:
        print("Testing operation 1...")
        zero_error()
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("Testing operation 2...")
        file_error()
    except FileNotFoundError:
        print("Caught FileNotFoundError: [Errno 2] No such file or directory: "
              "'non/existent/file'")
    try:
        print("Testing operation 3...")
        type_error()
    except (TypeError):
        print("Caught TypeError: can only concatenate str"
              " (not \"int\") to str")
    try:
        print("Testing operation 4...")
        mult()
        print("Operation completed successfully")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


def garden_operations():
    """
    Defines all the functions that will be used to test each type of errors
    there are.
    Returns: All the functions
    """
    def value_error() -> None:
        """
        Tries to convert the string "abc" to an int
        """
        int("abc")

    def zero_error() -> None:
        """
        Tries to divide 12 by 0
        """
        12 / 0

    def file_error() -> None:
        """
        Tries to open a non existent file
        """
        open("non/existent/file", "r")

    def type_error() -> None:
        """
        Tries to add a string and an int together
        """
        "num" + 2

    def mult() -> None:
        """
        This is a valid function, joining to strings together
        But is used to show how you can except multiple errors
        """
        "num" + "abc"
    return value_error, zero_error, file_error, type_error, mult


if __name__ == "__main__":
    test_error_types()
