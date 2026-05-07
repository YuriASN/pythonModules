#!/usr/bin/env python3

import sys


def output_file(file: str) -> None:
    try:
        print(f"Accessing file '{file}'")
        with open(file, "r") as opened:
            print("---\n")
            print(opened.read(), end="")
            print("\n---")
        print(f"File '{file}'closed.")
    except Exception as err:
        print(f"Error opening file '{file}': {err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        output_file(sys.argv[1])
