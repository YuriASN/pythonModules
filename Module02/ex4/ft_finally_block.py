class GardenError(Exception):
    """Base class for garden errors"""
    pass


class PlantError(GardenError):
    """Base class for plant errors"""
    def __init__(self, plant: str, error: str) -> None:
        if error is None:
            error = f"The {plant} plant is wilting!"
        super().__init__(error)


class WaterError(GardenError):
    """Base class for water errors"""
    def __init__(self, error: str) -> None:
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


def water_plant(plant_name: Plant) -> None:
    """Waters the plant if plant name is captalized"""


def test_watering_system() -> None:
    """Water several Plants using water_plant()"""