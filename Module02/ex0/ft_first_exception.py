def input_temperature(temp_str: str) -> int:
    """Returns the value as an int, if it's valid"""

    try:
        temp = int(temp_str)
        return temp
    except ValueError as display_error:
        raise ValueError(f"{display_error}")


def test_temperature() -> None:
    """Calls the input_temperature funtion with different values to test it.
    Outputing the value attempted and it's result."""

    print("=== Garden Temperature ===\n")
    temp: str = "25"
    print(f"Input data is '{temp}'")
    try:
        int_temp = input_temperature(temp)
    except ValueError as display_error:
        print(f"Caught input_temperature error: {display_error}")
    else:
        print(f"Temperature is now {int_temp}°C")

    print()

    temp: str = "abc"
    print(f"Input data is '{temp}'")
    try:
        int_temp = input_temperature(temp)
    except ValueError as display_error:
        print(f"Caught input_temperature error: {display_error}")
    else:
        print(f"Temperature is now {int_temp}°C")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
