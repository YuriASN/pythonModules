#!/usr/bin/env python3

import alchemy


def test_potions() -> None:
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    print("=== Distillation 1 ===\n" +
          "Using: 'import alchemy'structure to access potions")
    test_potions()
