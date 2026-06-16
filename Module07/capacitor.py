#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == "__main__":
    try:
        # Healing
        print("Testing Creature with healing capability")
        healing_f = HealingCreatureFactory()
        healing_f.create_base()
        print(f" base:\n{healing_f.base.describe()}\n"
              f"{healing_f.base.attack()}\n{healing_f.base.heal()}")
        healing_f.create_evolved()
        print(f" evolved:\n{healing_f.evolved.describe()}\n"
              f"{healing_f.evolved.attack()}\n{healing_f.evolved.heal()}")
        print()

        # Transformed
        print("Testing Creature with transform capability")
        trans_f = TransformCreatureFactory()
        trans_f.create_base()
        print(f" base:\n{trans_f.base.describe()}\n"
              f"{trans_f.base.attack()}\n"
              f"{trans_f.base.transform()}\n{trans_f.base.attack()}\n"
              f"{trans_f.base.revert()}")
        trans_f.create_evolved()
        print(f" evolved:\n{trans_f.evolved.describe()}\n"
              f"{trans_f.evolved.attack()}\n"
              f"{trans_f.evolved.transform()}\n{trans_f.evolved.attack()}\n"
              f"{trans_f.evolved.revert()}")
    except Exception as err:
        print(err)
