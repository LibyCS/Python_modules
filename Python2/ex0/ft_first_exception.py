def input_temperature(temp_str: str | int) -> int:
    """
    Take the string temp_str and converts it into an int and then returns
    the int form.
    """
    print(f"\nInput data is \'{temp_str}\'")
    temp_str = int(temp_str)
    print(f"Temperature is now {temp_str}°C")
    return temp_str


def test_temperature() -> None:
    """
    Testing different temperature inputs
    """
    print("=== Garden Temperature ===")
    input_temperature("25")
    try:
        input_temperature("abc")
    except ValueError:
        print("Caught input_temperature error: invalid literal"
              " for int() with base 10: \'abc\'")
    print("\nAll tests completed - program didn't crash!")


test_temperature()
