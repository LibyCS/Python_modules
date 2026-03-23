def input_temperature(temp_str: str | int) -> int:
    """
    Determines weather the temperature given is a valid number aswell as
    deciding weather the temperature is right or not for plants.
    Args:
        str_temp: takes in a tempertaure in a string input
    """
    print(f"\nInput data is \'{temp_str}\'")
    temp_int = int(temp_str)
    if temp_int < 0:
        raise Exception(f"Caught input_temperature error: {temp_int}°C"
                        " is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise Exception(f"Caught input_temperature error: {temp_int}°C"
                        " is too hot for plants (max 40°C)")
    print(f"Temperature is now {temp_int}°C")
    return (temp_int)


def test_temperature() -> None:
    """
    Testing different temperature inputs
    """
    print("=== Garden Temperature Checker ===")
    nums = ["25", "abc", "100", "-50"]
    for num in nums:
        try:
            input_temperature(num)
        except ValueError:
            print("Caught input_temperature error: invalid literal"
                  f" for int() with base 10: \'{num}\'")
        except Exception as m:
            print(m)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
