#!/usr/bin/env python3

import alchemy.transmutation


def test_trans() -> None:
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    print("=== Transmutation 1 ===\n" +
          "Import transmutation module directly")
    test_trans()
    print()
