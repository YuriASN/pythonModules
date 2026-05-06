#!/usr/bin/env pyhton3

from alchemy.elements import create_air


def test_create_air() -> None:
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    print("=== Alembic 3 ===\n" +
          "Accessing alchemy/elements.py using 'from ... import ...'structure")
    test_create_air()
    print()
