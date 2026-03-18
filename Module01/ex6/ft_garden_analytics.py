from typing import List


class Plant:
    def __init__(self, name: str, height: int, days_old: int):
        self.__name = name
        self.__height = 0
        self.__growth = 0
        self.__days_old = 0
        self.set_height(height)
        self.set_age(days_old)

    def get_type(self):
        return f"{self.__class__.__name__}"

    def grow(self) -> None:
        self.__growth += 1

    def get_growth(self):
        return self.__growth

    def age(self) -> None:
        self.__days_old += 1

    def get_name(self) -> str:
        return f"{self.__name}"

    def get_age(self) -> int:
        return self.__days_old

    def get_height(self) -> int:
        return self.__height + self.__growth

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

    def get_type(self):
        return f"{self.__class__.__name__}"

    def get_color(self) -> str:
        return f"{self.__color}"

    def bloom(self) -> str:
        if super().get_height() < 10:
            return (f"not blooming")
        else:
            return (f"blooming")

    def get_info(self) -> str:
        return (super().get_info() +
                f", {self.get_color()} flowers ({self.bloom()})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, days_old: int, color: str,
                 prize_pnts: int):
        super().__init__(name, height, days_old, color)
        self.__prize_p = prize_pnts

    def get_type(self):
        return f"{self.__class__.__name__}"

    def get_prize_points(self) -> int:
        return f"{self.__prize_p}"

    def set_prize_points(self, new_points) -> str:
        self.__prize_p = new_points

    def get_info(self) -> str:
        return (super().get_info() +
                f", Prize points: {self.get_prize_points()}")


class Garden():
    def __init__(self, owner: str, plants: List[Plant]):
        self.__owner = owner
        self.__plants = plants

    def get_owner(self):
        return f"{self.__owner}"

    def add_plant(self, new: Plant):
        self.__plants.append(new)
        print(f"Added {new.get_name()} to {self.get_owner()}'s garden")

    def total_gain(self):
        total_gain = 0
        for plant in self.__plants:
            total_gain += plant.get_growth()
        return total_gain

    def garden_report(self):
        plant_amount: int = 0
        class_count: List
        print(f"=== {self.get_owner()}'s Garden Report ===\n"
              f"Plants in garden:")
        for plant in self.__plants:
            print(f"- {plant.get_info()}")
            plant_amount += 1
            class_count[plant.get_type()] += 1
        print(f"\nPlants added: {self.__plants.count()}, "
              f"Total growth {self.total_gain()}cm")
        print(f"Plant types: ")
        for type in class_count:
            
        {} regular, "
              f"{} flowering, "
              f"{} prize flowers")

class GardenManager():
    def __init__(self, gardens: Garden):
        
    def create_garden_network():

    def GardenStats():