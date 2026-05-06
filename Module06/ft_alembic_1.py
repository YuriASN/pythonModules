#!/usr/bin/env pyhton3

from elements import create_water


def test_create_water() -> None:
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    print("=== Alembic 1 ===\n" +
          "Using: 'from ... import ...'structure to access elements.py")
    test_create_water()
    print()
