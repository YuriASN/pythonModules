#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days_old: int):
        self.name = name
        self.height = height
        self.days_old = days_old

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self, days_passed: int) -> None:
        self.days_old += days_passed

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")


def ft_plant_factory(new_plants: list[tuple]) -> list[Plant]:
    plants: list[Plant] = []
    print("=== Plant Factory Output ===")
    for p in new_plants:
        created = Plant(*p)
        print("Created: ", end="")
        created.show()
        plants.append(created)
    return plants


if __name__ == "__main__":
    garden = [("Rose", 25, 10),
              ("Tulip", 5, 3),
              ("Sunflower", 40, 30),
              ("Jacaranda", 50, 47),
              ("Oak", 30, 30)]
    new_plants = ft_plant_factory(garden)
