#!/usr/bin/env python3


def main() -> None:
    entries: list = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open("new_discovery.txt", "w") as file:
            print("Storage unit created successfully...\n\n"
                  "Inscribing preservation data...")
            file.write(entries[0] + "\n")
            print(entries[0])
            file.write(entries[1] + "\n")
            print(entries[1])
            file.write(entries[2] + "\n")
            print(entries[2])
        print("\nData inscription complete. Storage unit sealed.\n"
              "Archive 'new_discovery.txt' ready for long-term preservation.")
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        print("ERROR: Can't create/access storage unit")


if __name__ == "__main__":
    main()
