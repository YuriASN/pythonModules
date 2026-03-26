#!/usr/bin/env python3

class ProjectError(Exception):
    """Base of project exception errors"""
    pass


class LowTemp(ProjectError):
    """Exception error when the temperature is low"""

    def __init__(self, value: int) -> None:
        self.__value: int = value
        super().__init__(f"{value}ºC is too cold for plants (min 0°C)")


class HighTemp(ProjectError):
    """Exception error when the temperature is high"""

    def __init__(self, value: int) -> None:
        self.__value: int = value
        super().__init__(f"{value}ºC is too hot for the plants (max 40ºC)")


def input_temperature(temp_str: str) -> int:
    """Returns the value as an int, if it's valid"""

    try:
        temp = int(temp_str)
    except ValueError as display_error:
        raise ValueError(f"{display_error}")
    else:
        if temp < 0:
            raise LowTemp(temp)
        elif temp > 40:
            raise HighTemp(temp)
        return temp


def test_temperature() -> None:
    """Calls the input_temperature funtion with different values to test it.
    Outputing the value attempted and it's result."""

    print("=== Garden Temperature ===\n")
    temp_list: list[str] = ["25", "abc", "100", "-40"]
    for temp in temp_list:
        print(f"Input data is '{temp}'")
        try:
            int_temp = input_temperature(temp)
        except (ValueError, HighTemp, LowTemp) as display_error:
            print(f"Caught input_temperature error: {display_error}")
        else:
            print(f"Temperature is now {int_temp}°C")
        print()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
