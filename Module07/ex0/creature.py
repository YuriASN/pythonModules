from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = ""
        self.type: str = ""

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return f"{self.name} uses Ember"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Water gun"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Hydro pump"


class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_base(self) -> None:
        self.base: Creature

    @abstractmethod
    def create_evolved(self) -> None:
        self.evolved: Creature


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> None:
        self.base = Flameling()

    def create_evolved(self) -> None:
        self.evolved = Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> None:
        self.base = Aquabub()

    def create_evolved(self) -> None:
        self.evolved = Torragon()
