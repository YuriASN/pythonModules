#!/usr/bin/env python3


def try_access(file: str) -> None:
    """Tries to access the given file"""
    try:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        with open(file, "r"):
            print("SUCCESS: Archive recovered - " +
                  "``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files = ["not_existent.txt", "classified_data.txt", "standard_archive.txt"]
    for file in files:
        try_access(file)
        print()
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
