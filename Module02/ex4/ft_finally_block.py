class GardenError(Exception):
    """Base class for garden errors"""
    pass


class PlantError(GardenError):
    """Base class for plant errors"""
    def __init__(self, plant: str, error: str) -> None:
        error = f"Invalid plant name to water: '{plant}'"
        super().__init__(error)


class WaterError(GardenError):
    """Base class for water errors"""
    def __init__(self, error: str) -> None:
        if error is None:
            error = "Not enough water in the tank!"
        super().__init__(error)


class Plant:
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self._name = name
        self._height = height
        self._days_old = days_old
        self._water = 4

    def get_name(self) -> str:
        """Returns the name of the plant"""
        return f"{self._name}"

    def get_status(self) -> str:
        """Returns a string of the status of the plan,
        accordingly to the amount of water that it has"""
        if self._water < 5:
            return f"{self._name} is looking good"
        else:
            raise PlantError(self._name, None)

    def pass_time(self) -> None:
        """Pass 5 days, growing 1cm and losing 1 water"""
        self._days_old += 5
        self._height += 1
        self._water -= 1

    def watering(self) -> None:
        """Adds water by 1"""
        self._water += 1


def water_plant(plant: Plant) -> None:
    """Waters the plant if plant name is captalized"""
    name = plant.get_name()
    if name == name.capitalize():
        plant.watering()
        print(f"Watering {plant.get_name()}: [OK]")
    else:
        raise PlantError(plant.get_name(), None)


def test_watering_system(plants: list[Plant]) -> None:
    """Water several Plants using water_plant()"""

    try:
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:

    print("=== Garden Watering System ===\n")
    plants: list = [Plant("Tomato", 10, 10),
                    Plant("Lettuce", 10, 10),
                    Plant("Carrots", 10, 10)]
    print("Testing valid plants...")
    test_watering_system(plants)
    plants[1]._name = "lettuce"
    print("\nTesting invalid plants...")
    test_watering_system(plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
