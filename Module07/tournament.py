#!/usr/bin/env python3

from ex0 import CreatureFactory, AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, \
                DefensiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:
        print(f"*** Tournament ***\n{len(opponents)} opponents involved")
        for index_a in range(len(opponents) - 1):
            factory_a, strategy_a = opponents[index_a]
            factory_a.create_base()
            for index_b in range(index_a + 1, len(opponents), 1):
                factory_b, strategy_b = opponents[index_b]
                factory_b.create_base()
                print("\n* Battle *")
                print(f"{factory_a.base.describe()}\n vs.\n"
                      f"{factory_b.base.describe()}\n now fight!")
                strategy_a.act(factory_a.base)
                strategy_b.act(factory_b.base)
    except Exception as err:
        print(f"Battle error, aborting tournament: {err}")


if __name__ == "__main__":
    aqua_f = AquaFactory()
    flame_f = FlameFactory()
    healing_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    normal_s = NormalStrategy()
    aggresive_s = AggressiveStrategy()
    defensive_s = DefensiveStrategy()

    opponents = [(flame_f, normal_s),
                 (healing_f, defensive_s)]
    print("Tournament 0 (basic)\n [ (Flameling+Normal), (Healing+Defensive)")
    battle(opponents)

    opponents = [(flame_f, aggresive_s),
                 (healing_f, defensive_s)]
    print("\nTournament 1 (error)\n [ (Flameling+Aggressive), "
          "(Healing+Defensive) ]")
    battle(opponents)

    opponents = [(aqua_f, normal_s),
                 (healing_f, defensive_s),
                 (trans_f, aggresive_s)]
    print("\nTournament 2 (multiple)\n [ (Aquabub+Normal), "
          "(Healing+Defensive), (Transform+Aggressive) ]")
    battle(opponents)
