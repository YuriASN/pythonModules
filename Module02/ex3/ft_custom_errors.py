#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden errors"""
    pass


class PlantError(GardenError):
    """Base class for plant errors"""
    def __init__(self, error: str = "Unknown plant error") -> None:
        super().__init__(error)


class WaterError(GardenError):
    """Base class for water errors"""
    def __init__(self, error: str = "Unknown plant error") -> None:
        super().__init__(error)


class Plant:
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self._name = name
        self._height = height
        self._days_old = days_old
        self._water = 4

    def get_name(self) -> str:
        return f"{self._name}"

    def get_status(self) -> str:
        if self._water >= 5:
            return f"{self._name} is looking good"
        else:
            raise PlantError(f"The {self._name} plant is wilting!")

    def pass_time(self) -> None:
        """Pass 5 days, growing 1cm and losing 1 water"""
        self._days_old += 5
        self._height += 1
        self._water -= 1

    def watering(self) -> None:
        """Adds water by 1"""
        self._water += 1


class GardenManager():
    def __init__(self, plant: Plant) -> None:
        self._plant = plant
        self._water_tank = 0

    def water_plant(self):
        """Water the plant by 1"""
        if self._water_tank > 0:
            self._plant.watering()
            self._water_tank -= 1
        else:
            raise WaterError("Not enough water in the tank!")

    def get_plant(self) -> Plant:
        return self._plant


def raise_custom(manager: GardenManager) -> None:
    plant = manager.get_plant()
    try:
        print(plant.get_status())
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    print("\nTesting WaterError...")
    try:
        manager.water_plant()
    except WaterError as err:
        print(f"Caught WaterError: {err}")


def raise_gardenerror(manager: GardenManager) -> None:
    plant = manager.get_plant()
    try:
        print(plant.get_status())
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        manager.water_plant()
    except GardenError as err:
        print(f"Caught GardenError: {err}")


if __name__ == "__main__":
    """Runs the tester"""
    man = GardenManager(Plant("tomato", 10, 10))
    print("=== Custom Garden Errors Demo ===\n\n" +
          "Testing PlantError...")
    raise_custom(man)
    print("\nTesting catching all garden errors...")
    raise_gardenerror(man)
    print("\nAll custom error types work correctly!")
