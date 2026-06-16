#!/usr/bin/env pyhton3

import alchemy.elements


def test_create_earth() -> None:
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    print("=== Alembic 2 ===\n" +
          "Accessing alchemy/elements.py using 'import ...'structure")
    test_create_earth()
    print()
