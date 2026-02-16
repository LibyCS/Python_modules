def check_temperature(str_temp):
    """
    Determines weather the temperature given is a valid number aswell as
    deciding weather the temperature is right or not for plants.
    Args:
        str_temp: takes in a tempertaure in a string input
    """
    try:
        str_temp = int(str_temp)
    except TypeError:
        print(f"Error: \'{str_temp}\' is not a valid number", sep="")
        return
    if str_temp < 0:
        print(f"Error: {str_temp} °C is too cold for plants (min 0°C)", sep="")
    elif str_temp > 40:
        print(f"Error: {str_temp} °C is too hot for plants (max 40°C)", sep="")
    else:
        print(f"Temperature {str_temp} °C is perfect for plants!", sep="")


def test_temperature_input():
    """
    Testing different temperature inputs
    """
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
