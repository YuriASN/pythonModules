#!/usr/bin/env python3

import alchemy.transmutation.recipes


def test_trans() -> None:
    print("Testing lead to gold: " +
          f"{alchemy.transmutation.recipes.lead_to_gold()}")


if __name__ == "__main__":
    print("=== Transmutation 0 ===\n" +
          "Using file alchemy/transmutation/recipes.py directly")
    test_trans()
    print()
