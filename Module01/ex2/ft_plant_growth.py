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


def week_growth(plant: Plant) -> None:
    first_height = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.show()
        plant.grow(0.8)
        plant.age(1)
    print(f"Growth this week: +{plant.height - first_height:.0f}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    week_growth(rose)
