#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden errors"""
    pass


class PlantError(GardenError):
    """Base class for plant errors"""
    def __init__(self, plant: str, error: str | None) -> None:
        if error is None:
            error = f"The {plant} plant is wilting!"
        super().__init__(error)


class WaterError(GardenError):
    """Base class for water errors"""
    def __init__(self, error: str | None) -> None:
        if error is None:
            error = "Not enough water in the tank!"
        super().__init__(error)


class Plant:
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self.__name = name
        self.__height = height
        self.__days_old = days_old
        self.__water = 4

    def get_name(self) -> str:
        return f"{self.__name}"

    def get_status(self) -> str:
        if self.__water >= 5:
            return f"{self.__name} is looking good"
        else:
            raise PlantError(self.__name, None)

    def pass_time(self) -> None:
        """Pass 5 days, growing 1cm and losing 1 water"""
        self.__days_old += 5
        self.__height += 1
        self.__water -= 1

    def watering(self) -> None:
        """Adds water by 1"""
        self.__water += 1


class GardenManager():
    def __init__(self, plant: Plant) -> None:
        self.__plant = plant
        self.__water_tank = 0

    def water_plant(self):
        """Water the plant by 1"""
        if self.__water_tank > 0:
            self.__plant.watering()
            self.__water_tank -= 1
        else:
            raise WaterError(None)

    def get_plant(self) -> Plant:
        return self.__plant


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
