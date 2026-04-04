#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
            print("\nData recovery complete. Storage unit disconnected.")
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
