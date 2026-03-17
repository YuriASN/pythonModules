class Plant:
    def __init__(self, name: str, height: int, days_old: int):
        self.name = name
        self.height = height
        self.days_old = days_old

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days_old += 1

    def get_info(self) -> None:
        return f"{self.name}: {self.height}cm, {self.days_old} days old"


def week_growth(plant: Plant) -> None:
    first_height = plant.height
    print("=== Day 1 ===")
    print(plant.get_info())
    for i in range(1, 7):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    print(plant.get_info())
    print(f"Growth this week: +{plant.height - first_height}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 10, 20)
    week_growth(rose)
