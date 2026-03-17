def garden_intro(plant_type: str, height: str, days: str) -> None:
    print("Plant: " + plant_type)
    print("Height: " + height)
    print("Age: " + days + " days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    garden_intro("Rose", "25cm", "30")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
