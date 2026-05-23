from abc import ABC, abstractmethod
from ex0.creature import Creature, CreatureFactory


class HealCapability(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def heal(self, target: Creature | None = None) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip"

    def heal(self, target: Creature | None = None) -> str:
        if target is not None:
            return f"{self.name} heals {target.name} for a small amount"
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance"

    def heal(self, target: Creature | None = None) -> str:
        if target is not None:
            return f"{self.name} heals {target.name} for a large amount"
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()
        self.base: Sproutling
        self.evolved: Bloomelle

    def create_base(self) -> None:
        self.base = Sproutling()

    def create_evolved(self) -> None:
        self.evolved = Bloomelle()


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Shiftling"
        self.type = "Normal"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Morphagon"
        self.type = "Normal/Dragon"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()
        self.base: Shiftling
        self.evolved: Morphagon

    def create_base(self) -> None:
        self.base = Shiftling()

    def create_evolved(self) -> None:
        self.evolved = Morphagon()
