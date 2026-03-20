class Plant:
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self.__name: str = name
        self.__height: int = 0
        self.__growth: int = 0
        self.__days_old: int = 0
        self.set_height(height)
        self.set_age(days_old)

    def grow(self, size: int) -> str:
        if size > 0:
            self.__growth += size
            return f"{self.__name} grew {size}cm"

    def age(self, days: int) -> str:
        if days > 0:
            self.__days_old += days
            return (f"{self.__name} aged {days} days, " +
                    f"and it's now {self.__days_old} days old")

    def get_name(self) -> str:
        return f"{self.__name}"

    def get_age(self) -> int:
        return self.__days_old

    def get_height(self) -> int:
        return self.__height + self.__growth

    def get_growth(self) -> int:
        return self.__growth

    def get_type(self) -> str:
        return f"{self.__class__.__name__}"

    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self.__days_old = new_age
        else:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]"
                  f"\nSecurity: Negative age rejected\n\nCurrent plant: "
                  f"{self.__name} ({self.__height}cm, {self.__days_old} days)")

    def set_height(self, new_height: int) -> None:
        if new_height > 0:
            self.__height = new_height
        else:
            print(f"\nInvalid operation attempted: height {new_height}cm "
                  f"[REJECTED]\nSecurity: Negative height rejected")

    def get_info(self) -> str:
        return (f"{self.__name}: {self.__height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, days_old: int, color: str):
        super().__init__(name, height, days_old)
        self.__color = color

    def get_color(self) -> str:
        return f"{self.__color}"

    def bloom(self) -> str:
        if self.get_age() < 10:
            return "not blooming"
        else:
            return "blooming"

    def get_info(self) -> str:
        return (super().get_info() +
                f", {self.get_color()} flowers ({self.bloom()})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 days_old: int, color: str, prize: int):
        super().__init__(name, height, days_old, color)
        self.__prize = prize

    def get_prize_points(self) -> int:
        return self.__prize

    def get_info(self) -> str:
        return (super().get_info() +
                f", Prize points: {self.get_prize_points()}")


#class GardenManager():

#    class GardenStats():


if __name__ == "__main__":
    pflower = PrizeFlower("Rose", 10, 10, "Blue", 10)
    nflower = FloweringPlant("Tulip", 5, 5, "white")
    plant = Plant("Avocado Tree", 50, 100)
    print(f"Type of pflower = {pflower.get_type()}\n"
          f"Type of nflower = {nflower.get_type()}\n"
          f"Type of plant = {plant.get_type()}")
