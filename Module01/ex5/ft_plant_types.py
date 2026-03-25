#!/usr/bin/env python3

class Plant:
    """Base class for any type of plant"""

    def __init__(self, name: str, height: float, days_old: int):
        self._name = name
        self._height: float = 0
        self._days_old: int = 0
        if height > 0:
            self._height = height
        self._days_old = 0
        if days_old > 0:
            self._days_old = days_old

    def grow(self, growth: float) -> None:
        """Grow the plant by 'growth' centimeters"""
        self._height += growth

    def age(self, days_passed: int) -> None:
        """Age the plant by 'days_passed' days"""
        self._days_old += days_passed

    def show(self) -> None:
        """Print the full data of the plant"""
        print(f"{self._name}: {self._height:.1f}cm, "
              f"{self._days_old} days old")

    def get_name(self) -> str:
        """Return the name of the plant"""
        return f"{self._name}"

    def get_age(self) -> int:
        """Return the age of the plant"""
        return self._days_old

    def get_height(self) -> float:
        """Return the height of the plant"""
        return self._height

    def set_age(self, new_age: int) -> None:
        """Set the age (new_age) for the plant.
        If new-age has a valid value"""

        if new_age > 0:
            self._days_old = new_age
            print(f"Age updated: {self._days_old} days")
        else:
            print(f"{self._name}: Error, age can't be negative\n"
                  f"Age update rejected")

    def set_height(self, new_height: int) -> None:
        """Set the height (new_height) of the plant.
        If new_height is a valid value"""

        if new_height > 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative\n"
                  f"Height update rejected")


class Flower(Plant):
    """Flower class that inherits from Plant class"""

    def __init__(self, name: str, height: float, days_old: int, color: str):
        super().__init__(name, height, days_old)
        self._color = color
        self._bloom = False

    def get_color(self) -> str:
        """Returns the color of the flower"""
        return f"{self._color}"

    def bloom(self) -> None:
        """Change status of flower bloom to true"""
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        if self._bloom:
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")


class Tree(Plant):
    """Tree class that inherits from Plant class"""

    def __init__(self, name: str, height: float, days: int, trunk_diam: int):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diam

    def get_trunk_diam(self) -> int:
        """Return the diameter of the trunk of the tree."""
        return self._trunk_diameter

    def produce_shade(self) -> None:
        """Print a string telling the shade that the tree is producing"""

        if self.get_height() <= 0:
            print(f"{self.get_name()} isn't high enough to produce a shade.")
        elif self._trunk_diameter <= 0:
            print(f"{self.get_name()} isn't large enough to produce a shade.")
        else:
            print(f"Tree {self.get_name()} now produces a shade of "
                  f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm"
                  f" wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.get_trunk_diam():.1f}cm")


class Vegetable(Plant):
    """Vegetable class that inherits from Plant class"""

    def __init__(self, name: str, height: float, days_old: int,
                 harvest_season: str):
        super().__init__(name, height, days_old)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self, days_passed: int) -> None:
        """Age the plant by 'days_passed' days,
        and add the same amount for nutritional value"""
        self._nutritional_value += days_passed
        super().age(days_passed)

    def grow(self, growth: float) -> None:
        # self._nutritional_value += 1
        super().grow(growth)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    garden: dict = {"flower": Flower("Rose", 15, 10, "pink"),
                    "tree": Tree("Oak", 200, 365, 5),
                    "vegetable": Vegetable("Tomato", 5, 10, "April")}
    print("=== Flower")
    garden["flower"].show()
    print("[asking the rose to bloom]")
    garden["flower"].bloom()
    garden["flower"].show()

    print("\n=== Tree")
    garden["tree"].show()
    print("[asking the oak to produce shade]")
    garden["tree"].produce_shade()

    print("\n=== Vegetable")
    garden["vegetable"].show()
    print("[make tomato grow and age for 20 days]")
    garden["vegetable"].grow(42)
    garden["vegetable"].age(20)
    garden["vegetable"].show()


if __name__ == "__main__":
    main()
