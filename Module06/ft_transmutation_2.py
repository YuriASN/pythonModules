#!/usr/bin/env python3

import alchemy


def test_trans() -> None:
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")


if __name__ == "__main__":
    print("=== Transmutation 2 ===\n" +
          "Import alchemy module only")
    test_trans()
