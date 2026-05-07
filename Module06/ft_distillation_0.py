#!/usr/bin/env python3

from alchemy.potions import strength_potion, healing_potion


def test_potions() -> None:
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    print("=== Distillation 0 ===\n" +
          "Direct access to alchemy/potions.py")
    test_potions()
    print()
