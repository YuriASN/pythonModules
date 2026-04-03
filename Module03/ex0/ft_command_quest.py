#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    args = sys.argv[1:]
    print(f"Program name: {sys.argv[0]}")
    if len(args) < 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        i = 0
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(args) + 1}")


if __name__ == "__main__":
    main()
