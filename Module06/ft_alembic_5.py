#!/usr/bin/env python3

from alchemy import create_air


def test_create_air() -> None:
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    print("=== Alembic 5 ===\n" +
          "Accessing the alchemy module using 'from alchemy import ...'")
    test_create_air()
