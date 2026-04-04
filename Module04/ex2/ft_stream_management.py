#!/usr/bin/env python3


import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    id = sys.stdin.readline().strip()
    print("Input Stream active. Enter status report: ", end="", flush=True)
    report = sys.stdin.readline().strip()
    print()
    sys.stdout.write(f"STANDARD] Archive status from {id}: {report}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
