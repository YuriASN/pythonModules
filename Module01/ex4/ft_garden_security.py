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


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25, 40)
    plant1.show()
    print()
    plant1.set_height(123)
    plant1.set_age(456)
    print()
    plant1.set_age(-123)
    plant1.set_height(-254)
    print()
    print("Current state: ", end="")
    plant1.show()


if "__main__" == __name__:
    ft_garden_security()
