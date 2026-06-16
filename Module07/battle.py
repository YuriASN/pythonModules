#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    try:
        factory.create_base()
        print(factory.base.describe())
        print(factory.base.attack())
        factory.create_evolved()
        print(factory.evolved.describe())
        print(factory.evolved.attack())
    except Exception as err:
        Exception(f"Testing factory: {err}")


def test_battle(factory_a: CreatureFactory,
                factory_b: CreatureFactory) -> None:
    try:
        print(factory_a.base.describe())
        print(" vs.")
        print(factory_b.base.describe())
        print(" fight!")
        print(factory_a.base.attack())
        print(factory_b.base.attack())
    except Exception as err:
        raise Exception(f"Testing battle: {err}")


if __name__ == "__main__":
    try:
        print("Testing factory")
        flame_f = FlameFactory()
        test_factory(flame_f)
        print()

        print("Testing factory")
        aqua_f = AquaFactory()
        test_factory(aqua_f)
        print()

        print("Testing battle")
        test_battle(flame_f, aqua_f)
    except Exception as err:
        print(err)
