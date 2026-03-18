class SecurePlant:
    def __init__(self, name: str, height: int, days_old: int):
        self.__name = name
        print(f"Plant created: {self.__name}")
        self.__height = 0
        self.__days_old = 0
        self.set_height(height)
        self.set_age(days_old)
        print()

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
            print(f"Age updated: {self.__days_old} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]"
                  f"\nSecurity: Negative age rejected\n\nCurrent plant: "
                  f"{self.__name} ({self.__height}cm, {self.__days_old} days)")

    def set_height(self, new_height: int) -> None:
        if new_height > 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {new_height}cm "
                  f"[REJECTED]\nSecurity: Negative height rejected"
                  f"\n\nCurrent plant: "
                  f"{self.__name} ({self.__height}cm, {self.__days_old} days)")

    def get_info(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__days_old} days old"


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 25, 40)
    plant3 = SecurePlant("Error", -13, 10)
    plant4 = SecurePlant("Error2", 19, -1)
    print(plant3.get_info())
    print(f"{plant4.get_info()}\n")

    print(plant1.get_info())
    plant1.age()
    plant1.grow()
    print(plant1.get_info())

    plant1.set_age(123)
    plant1.set_height(254)
    print(plant1.get_info())

    plant1.set_age(-123)
    plant1.set_height(-254)
    print(plant1.get_info())


if "__main__" == __name__:
    ft_garden_security()
