class Plant:
    def __init__(self, name: str, height: int, days_old: int) -> None:
        self.__name: str = name
        self.__height: int = 0
        self.__growth: int = 0
        self.__days_old: int = 0
        self.set_height(height)
        self.set_age(days_old)

    def grow(self, size: int) -> str:
        if size > 0:
            self.__growth += size
            return f"{self.__name} grew {size}cm"

    def age(self, days: int) -> str:
        if days > 0:
            self.__days_old += days
            return (f"{self.__name} aged {days} days, " +
                    f"and it's now {self.__days_old} days old")

    def get_name(self) -> str:
        return f"{self.__name}"

    def get_age(self) -> int:
        return self.__days_old

    def get_height(self) -> int:
        return self.__height + self.__growth

    def get_growth(self) -> int:
        return self.__growth

    def get_type(self) -> str:
        return f"{self.__class__.__name__}"

    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self.__days_old = new_age
        else:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]"
                  f"\nSecurity: Negative age rejected\n\nCurrent plant: "
                  f"{self.__name} ({self.__height}cm, {self.__days_old} days)")

    def set_height(self, new_height: int) -> None:
        if new_height > 0:
            self.__height = new_height
        else:
            print(f"\nInvalid operation attempted: height {new_height}cm "
                  f"[REJECTED]\nSecurity: Negative height rejected")

    def get_info(self) -> str:
        return (f"{self.__name}: {self.__height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, days_old: int, color: str):
        super().__init__(name, height, days_old)
        self.__color = color

    def get_color(self) -> str:
        return f"{self.__color}"

    def bloom(self) -> str:
        if self.get_age() < 10:
            return "not blooming"
        else:
            return "blooming"

    def get_info(self) -> str:
        return (super().get_info() +
                f", {self.get_color()} flowers ({self.bloom()})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 days_old: int, color: str, prize: int):
        super().__init__(name, height, days_old, color)
        self.__prize = prize

    def get_prize_points(self) -> int:
        return self.__prize

    def get_info(self) -> str:
        return (super().get_info() +
                f", Prize points: {self.get_prize_points()}")


class Garden:
    def __init__(self, owner: str, plants: list[Plant]) -> None:
        self.__owner: str = owner
        self.__plants: list[Plant] = plants
        self.__plant_amount = 0
        for plant in plants:
            self.__plant_amount += 1

    def get_owner(self) -> str:
        return f"{self.__owner}"

    def get_plants(self) -> list[Plant]:
        return self.__plants

    def get_amount_plants(self) -> int:
        return self.__plant_amount

    def add_plant(self, plant: Plant) -> None:
        self.__plants += [plant]
        self.__plant_amount += 1

    def all_height(self) -> int:
        total: int = 0
        for plant in self.__plants:
            total += plant.get_height()
        return total

    def all_growth(self) -> int:
        total: int = 0
        for plant in self.__plants:
            total += plant.get_growth()
        return total

    def all_prize(self) -> int:
        total: int = 0
        for plant in self.__plants:
            if plant.get_type() == "PrizeFlower":
                total += plant.get_prize_points()
        return total

    def reset_plants(self, new_list: list[Plant]) -> None:
        self.__plants = new_list


class GardenManager:
    """Creates a Garden Manager that manages plants and statistics"""

    def __init__(self, gardens: list[Garden]):
        self.__gardens: list[Garden] = []
        self.__total_gardens = 0
        for garden in gardens:
            self.add_garden(garden)

    class GardenStats:
        """Nested class to calulate analitics"""

        def report(garden: Garden) -> None:
            plants = garden.get_plants()
            owner = garden.get_owner()
            type_count: dict[str, int] = {"Plant": 0,
                                          "FloweringPlant": 0,
                                          "PrizeFlower": 0}
            print(f"=== {owner}'s Garden Report ===\n"
                  f"Plants in garden:")
            for plant in plants:
                print(f"- {plant.get_name()}: {plant.get_info()}")
                type_count[plant.get_type()] += 1
            print(f"\nPlants added: {garden.get_amount_plants()}, "
                  f"Total growth: {garden.all_growth()}cm")
            print(f"Plant types: {type_count["Plant"]} regular, "
                  f"{type_count["FloweringPlant"]} flowering, "
                  f"{type_count["PrizeFlower"]} prize flower")

    def report(self, owner: str) -> None:
        """Calls function of helper class passing the Garden as argument"""
        for garden in self.__gardens:
            if garden.get_owner() == owner:
                self.GardenStats.report(garden)

    def add_garden(self, garden: Garden) -> None:
        """Add garden to be managed"""
        self.__gardens += [garden]
        self.__total_gardens += 1

    def grow_all(self, owner: str, growth: int) -> None:
        """Grow all the plants from owner's garden by `growth` centimeters"""
        if growth < 1:
            pass
        for garden in self.__gardens:
            if garden.get_owner() == owner:
                print(f"{garden.get_owner()} is helping all plants grow...")
                for plant in garden.get_plants():
                    plant.grow(growth)
                    print(f"{plant.get_name()} grew {growth}cm")

    def gardens_managed(self) -> int:
        """Returns the amount of gardens being managed"""
        return self.__total_gardens

    def add_plant(self, owner: str, plant: Plant) -> None:
        """Adds the plant to the owner's garden"""
        for garden in self.__gardens:
            if garden.get_owner() == owner:
                garden.add_plant(plant)
                print(f"Added {plant.get_name()} to {owner}'s garden")
                return
            print(f"{owner}'s garden doesn't exist!")

    def del_plant(self, owner: str, remove: str) -> None:
        """Re-do the plant list on owner's garden removing any 'delete'"""
        for garden in self.__gardens:
            if garden.get_owner() == owner:
                plants = garden.get_plants()
                new_list = [
                    plant for plant in plants
                    if plant.get_name() != remove
                ]
                garden.reset_plants(new_list)
                break

    def del_garden(self, owner: str):
        """Remove the garden of the owner"""
        self.__gardens = [
            garden for garden in self.__gardens
            if garden.get_owner() != owner
                        ]

    def scores(self) -> None:
        """Print the scores for each garden managed"""
        amount = self.__total_gardens
        print("Garden scores - ", end="")
        i = 0
        for garden in self.__gardens:
            score: int = 0
            for plant in garden.get_plants():
                score += plant.get_height() + (plant.get_growth() * 10)
                if plant.get_type() == "PrizeFlower":
                    score += plant.get_prize_points()
            print(f"{garden.get_owner()}: {score}",
                  end=", " if i < amount - 1 else "\n")
            i += 1

    @staticmethod
    def height_validation(height: int) -> str:
        """Validates if height value is positive"""
        if height < 0:
            return "False"
        else:
            return "True"

    @classmethod
    def create_garden_network(cls,
                              gardens: list[Garden]
                              ) -> list["GardenManager"]:
        """Creates a manager per garden????"""
        managers: list["GardenManager"] = []
        for garden in gardens:
            managers += [cls(garden)]
        return managers


if __name__ == "__main__":
    manager = GardenManager(
        [Garden("Yuri", [
                        PrizeFlower("Rose", 10, 10, "Blue", 10),
                        FloweringPlant("Tulip", 5, 5, "white"),
                        Plant("Avocado Tree", 50, 100)
                        ]
                )]
    )
    manager.add_garden(Garden("Cat", [
        Plant("Orange Tree", 100, 50)
    ]))
    manager.add_garden(Garden("Mari", [
        Plant("Narcisus", 10, 55)
    ]))
    print("=== Garden Management System Demo ===\n")
    manager.add_plant("Yuri", Plant("Oak Tree", 100, 30))
    manager.add_plant("Yuri", FloweringPlant("Rose", 25, 30, "red"))
    manager.add_plant("Yuri", PrizeFlower("Sunflower", 50, 30, "yellow", 10))
    print()
    manager.del_plant("Yuri", "Tulip")
    manager.grow_all("Yuri", 5)
    print()
    manager.report("Yuri")
    print()
    print(f"Height validation test: {manager.height_validation(10)}")
    manager.scores()
    print(f"Total gardens managed: {manager.gardens_managed()}")
