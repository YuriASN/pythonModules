#!/usr/bin/env pyhton3

import elements


def test_create_fire() -> None:
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    print("=== Alembic 0 ===\n" +
          "Using: 'import ...'structure to access elements.py")
    test_create_fire()
    print()
