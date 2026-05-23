from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Ivalid Creature '{creature.name}' for this "
                            "normal strategy")
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, Creature):
            return False
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(f"{creature.transform()}\n{creature.attack()}\n"
                  f"{creature.revert()}")
        else:
            raise Exception(f"Ivalid Creature '{creature.name}' for this "
                            "aggresive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, TransformCapability):
            return False
        return True


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(f"{creature.attack()}\n{creature.heal()}")
        else:
            raise Exception(f"Ivalid Creature '{creature.name}' for this "
                            "defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, HealCapability):
            return False
        return True
