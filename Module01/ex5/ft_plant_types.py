#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days_old: int):
        self._name = name
        self._height = 0
        if height > 0:
            self._height = height
        self._days_old = 0
        if days_old > 0:
            self._days_old = days_old

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, days_passed: int) -> None:
        self.days_old += days_passed

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, "
              f"{self._days_old} days old")

    def get_name(self) -> str:
        return f"{self._name}"

    def get_age(self) -> int:
        return self._days_old

    def get_height(self) -> int:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self._days_old = new_age
            print(f"Age updated: {self._days_old} days")
        else:
            print(f"{self._name}: Error, age can't be negative\n"
                  f"Age update rejected")

    def set_height(self, new_height: int) -> None:
        if new_height > 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative\n"
                  f"Height update rejected")


class Flower(Plant):
    def __init__(self, name: str, height: int, days_old: int, color: str):
        super().__init__(name, height, days_old)
        self._color = color

    def get_color(self) -> str:
        return f"{self._color}"

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
        self._trunk_diam = trunk_diam

    def get_trunk_diam(self) -> int:
        return self._trunk_diam

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
        self._harvest_s = harvest_season
        self._nutri_value = nutritional_value

    def get_harvest(self) -> str:
        return self._harvest_s

    def get_nutri_value(self) -> str:
        return f"{self.get_name()} is rich in {self._nutri_value}"

    def get_info(self) -> str:
        return (super().get_info() + f", {self.get_harvest()} harvest")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    garden_data: list = [(Flower, "Rose", 10, 9, "pink"),
                         (Flower, "Narcisus", 15, 10, "red"),
                         (Tree, "Jacaranda", 200, 3650, 50),
                         (Tree, "Oak", 86, 365, 25),
                         (Vegetable, "Carrot", 5, 8, "fall", "beta-carotene"),
                         (Vegetable, "Lettuce", 25, 30, "summer", "vitamin K")]
    garden: list = [plant[0](*plant[1:]) for plant in garden_data]
    for plant in garden:
        print()
        print(plant.get_info())
        if plant.get_type() == "Flower":
            print(plant.bloom())
        elif plant.get_type() == "Tree":
            print(plant.produce_shade())
        if plant.get_type() == "Vegetable":
            print(plant.get_nutri_value())


if __name__ == "__main__":
    ft_plant_types()
