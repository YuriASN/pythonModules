#!/usr/bin/env python3

class Plant:
    """Base class for any type of plant"""

    def __init__(self, name: str, height: float, days_old: int):
        self._name = name
        self._height = 0
        self._days_old = 0
        if height > 0:
            self._height = height
        self._days_old = 0
        if days_old > 0:
            self._days_old = days_old
        self._stats = self.Stats()

    class Stats:
        """Nested helper class to hold statistics of called functions"""
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def age(self) -> None:
            self._age_count += 1

        def grow(self) -> None:
            self._grow_count += 1

        def show(self) -> None:
            self._show_count += 1

        def show_stats(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, "
                  f"{self._show_count} show")

    @classmethod
    def unknown(cls) -> "Plant":
        """Creates a plant without attributes."""
        return cls("Unknown plant", 0, 0)

    def grow(self, growth: float) -> None:
        """Grow the plant by 'growth' centimeters"""
        self._height += growth
        self._stats.grow()

    def age(self, days_passed: int) -> None:
        """Age the plant by 'days_passed' days"""
        self._days_old += days_passed
        self._stats.age()

    def show(self) -> None:
        """Print the full data of the plant"""
        print(f"{self._name}: {self._height:.1f}cm, "
              f"{self._days_old} days old")
        self._stats.show()

    def stats(self) -> None:
        self._stats.show_stats()

    def get_name(self) -> str:
        """Return the name of the plant"""
        return f"{self._name}"

    def get_age(self) -> int:
        """Return the age of the plant"""
        return self._days_old

    @staticmethod
    def check_year_old(age: int) -> bool:
        """Checks if 'age' is older than an year"""
        if age > 365:
            return True
        else:
            return False

    def set_age(self, new_age: int) -> None:
        """Set the age (new_age) for the plant.
        If new-age has a valid value"""

        if new_age > 0:
            self._days_old = new_age
            print(f"Age updated: {self._days_old} days")
        else:
            print(f"{self._name}: Error, age can't be negative\n"
                  f"Age update rejected")

    def get_height(self) -> int:
        """Return the height of the plant"""
        return self._height

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

    def bloom(self) -> str:
        """Change status of flower bloom to true"""
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        if self._bloom:
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")


class Seed(Flower):
    """Seed class that inherits from Flower class.
    Stores the seeds when a flower has bloomed."""
    def __init__(self, name: str, height: float, days_old: int,
                 color: str) -> None:
        super().__init__(name, height, days_old, color)
        self._seed = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed}")


class Tree(Plant):
    """Tree class that inherits from Plant class"""

    def __init__(self, name: str, height: float, days: int, trunk_diam: int):
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diam

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def produce_shade(self) -> None:
            self._shade_count += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self._shade_count} shade")

    def get_trunk_diam(self) -> int:
        """Return the diameter of the trunk of the tree."""
        return self._trunk_diameter

    def produce_shade(self) -> str:
        """Print a string telling the shade that the tree is producing"""

        if self.get_height() <= 0:
            print(f"{self.get_name()} isn't high enough to produce a shade.")
        elif self._trunk_diameter <= 0:
            print(f"{self.get_name()} isn't large enough to produce a shade.")
        else:
            self._stats.produce_shade()
            print(f"Tree {self.get_name()} now produces a shade of "
                  f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm"
                  f" wide.")

    def show(self) -> None:
        super().show()
        print(f" {self.get_trunk_diam():.1f}cm diameter")


def main() -> None:
    print("=== Garden statistics ===")

    garden: dict = {"flower": Flower("Rose", 15, 10, "pink"),
                    "tree": Tree("Oak", 200, 365, 5),
                    "seed": Seed("Sunflower", 80, 45, "yellow")}

    print("=== Check year-old")
    days = 30
    print(f"Is {days} days more than a year? -> "
          f"{garden["flower"].check_year_old(days)}")
    days = 400
    print(f"Is {days} days more than a year? -> "
          f"{garden["flower"].check_year_old(days)}")

    print("\n=== Flower")
    garden["flower"].show()
    print("[statistics for Rose]")
    garden["flower"].stats()
    print("[asking the rose to grow and bloom]")
    garden["flower"].grow(8)
    garden["flower"].bloom()
    garden["flower"].show()
    print("[statistics for Rose]")
    garden["flower"].stats()

    print("\n=== Tree")
    garden["tree"].show()
    print("[statistics for Oak]")
    garden["tree"].stats()
    print("[asking the oak to produce shade]")
    garden["tree"].produce_shade()
    print("[statistics for Oak]")
    garden["tree"].stats()

    print("\n=== seed")
    garden["seed"].show()
    print("[make sunflower grow, age and bloom]")
    garden["seed"].grow(30)
    garden["seed"].age(20)
    garden["seed"].bloom()
    garden["seed"].show()
    garden["seed"].stats()

    anon = Plant.unknown()
    print("\n=== Anonymous")
    anon.show()
    print("[statistics for Unknown plant]")
    anon.stats()


if __name__ == "__main__":
    main()
