#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data(garden: list[Plant]) -> None:
    print("=== Garden Plant Registry ===")
    for i in garden:
        i.show()


def main() -> None:
    plant1 = Plant("Roses", 15, 9)
    plant2 = Plant("Sunflower", 34, 6)
    plant3 = Plant("Tulips", 2, 3)
    garden: list[Plant] = [plant1, plant2, plant3]
    ft_garden_data(garden)


if __name__ == "__main__":
    main()
