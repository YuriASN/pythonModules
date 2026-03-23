class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(garden: list[Plant]) -> None:
    print("=== Garden Plant Registry ===")
    for i in garden:
        print(f"{i.name}: {i.height}cm, {i.age} days old")


def main() -> None:
    plant1 = Plant("Roses", 15, 9)
    plant2 = Plant("Sunflower", 34, 6)
    plant3 = Plant("Tulips", 2, 3)
    garden: list[Plant] = [plant1, plant2, plant3]
    ft_garden_data(garden)


if __name__ == "__main__":
    main()
