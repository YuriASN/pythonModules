from typing import List


class Plant:
    def __init__(self, name: str, height: int, days_old: int):
        self.__name = name
        self.__height = 0
        self.__days_old = 0
        self.set_height(height)
        self.set_age(days_old)

    def grow(self) -> None:
        self.__height += 1

    def age(self) -> None:
        self.__days_old += 1

    def get_name(self) -> str:
        return f"{self.__name}"

    def get_age(self) -> int:
        return self.__days_old

    def get_height(self) -> int:
        return self.__height

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
        return (f"{self.__name} ({self.__class__.__name__}): "
                f"{self.__height}cm, {self.__days_old} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, days_old: int, color: str):
        super().__init__(name, height, days_old)
        self.__color = color

    def get_color(self) -> str:
        return f"{self.__color}"

    def bloom(self) -> str:
        if self.get_age() < 10:
            return (f"{self.get_name()} is {self.get_age()} days old. "
                    f"It's too young to bloom!")
        else:
            return (f"{self.get_name()} is blooming beautifully!")

    def get_info(self) -> str:
        return (super().get_info() + f", {self.get_color()} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, days_old: int, trunk_diam: int):
        super().__init__(name, height, days_old)
        self.__trunk_diam = trunk_diam

    def get_trunk_diam(self) -> int:
        return self.__trunk_diam

    def produce_shade(self) -> str:
        if self.get_height() <= 0:
            return f"{self.get_name()} isn't high enough to produce a shade."
        else:
            return (f"{self.get_name()} provides "
                    f"{self.get_height() * 0.03:.0f} square meters of shade")

    def get_info(self) -> str:
        return (super().get_info() + f", {self.get_trunk_diam()}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days_old: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, days_old)
        self.__harvest_s = harvest_season
        self.__nutri_value = nutritional_value

    def get_harvest(self) -> str:
        return self.__harvest_s

    def get_nutri_value(self) -> str:
        return f"{self.get_name()} is rich in {self.__nutri_value}"

    def get_info(self) -> str:
        return (super().get_info() + f", {self.get_harvest()} harvest")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    garden_data: List = [(Flower, "Rose", 10, 9, "pink"),
                         (Flower, "Narcisus", 15, 10, "red"),
                         (Tree, "Jacaranda", 200, 3650, 50),
                         (Tree, "Oak", 86, 365, 25),
                         (Vegetable, "Carrot", 5, 8, "fall", "beta-carotene"),
                         (Vegetable, "Lettuce", 25, 30, "summer", "vitamin K")]
    garden: List = [plant[0](*plant[1:]) for plant in garden_data]
    for plant in garden:
        print()
        print(plant.get_info())
        if plant.__class__.__name__ == "Flower":
            print(plant.bloom())
        elif plant.__class__.__name__ == "Tree":
            print(plant.produce_shade())
        if plant.__class__.__name__ == "Vegetable":
            print(plant.get_nutri_value())


if __name__ == "__main__":
    ft_plant_types()
