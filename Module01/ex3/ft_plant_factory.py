class Plant:
    def __init__(self, name: str, height: int, days_old: int):
        self.name = name
        self.height = height
        self.days_old = days_old

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days_old += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.days_old} days old"


def ft_plant_factory(new_plants: list[tuple]) -> list[Plant]:
    total = 0
    plants: list[Plant] = []
    print("=== Plant Factory Output ===")
    for p in new_plants:
        created = Plant(*p)
        print(f"Created: {created.name} "
              f"({created.height}cm, {created.days_old} days)")
        total += 1
        plants.append(created)
    print(f"\nTotal plants created: {total}")
    return plants


if __name__ == "__main__":
    garden = [("Rose", 25, 10),
              ("Tulip", 5, 3),
              ("Sunflower", 40, 30),
              ("Jacaranda", 50, 47),
              ("Oak", 30, 30)]
    new_plants = ft_plant_factory(garden)
    print(f"Garden has from {new_plants[0].name} to {new_plants[4].name}")
