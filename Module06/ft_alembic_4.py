#!/usr/bin/env python3

import alchemy


def test_create_air() -> None:
    print(f"Testing create_air: {alchemy.create_air()}")


def test_create_earth() -> None:
    # Have a mypy error stated on subject's page 8
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")


if __name__ == "__main__":
    try:
        print("=== Alembic 4 ===\n" +
              "Accessing the alchemy module using 'import alchemy'")
        test_create_air()
        print("Now show that not all functions can be reached\n"
              "This will raise an exception!")
        test_create_earth()
    except Exception as err:
        print(f"Exception being raised: {err}")
    finally:
        print()
