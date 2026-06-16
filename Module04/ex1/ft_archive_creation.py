#!/usr/bin/env python3

import sys


def output_file(file: str) -> None:
    transformed: str = ""
    try:
        print(f"Accessing file '{file}'")
        opened = open(file, "r")
        print("---\n")
        line = opened.readline()
        while line:
            print(line)
            transformed += line.rstrip("\n") + "#"
            if line[-1] == "\n":
                transformed += "\n"
            line = opened.readline()
        print("\n---")
        opened.close()
        print(f"File '{file}'closed.\n")
    except Exception as err:
        raise Exception(f"Error opening file '{file}': {err}")
    try:
        print("Transform data:\n---\n")
        print(transformed)
        print("\n---")
        trans_file = input("Enter new file name (or empty): ")
        if trans_file:
            print(f"Saving data to '{trans_file}'")
            opened = open(trans_file, "w")
            opened.write(transformed)
            opened.close()
            print(f"Data saved in file '{trans_file}'")
        else:
            print("Not saving data.")
    except Exception as err:
        raise Exception(f"Writting transformed data to file: {err}")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
        else:
            print("=== Cyber Archives Recovery ===")
            output_file(sys.argv[1])
            print()
    except Exception as err:
        print(err)
