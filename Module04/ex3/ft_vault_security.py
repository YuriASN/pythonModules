#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        print("Vault connection established with failsafe protocols\n\n"
              "SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as file:
            print(file.read())
        print("\nSECURE PRESERVATION:")
        with open("preservated.txt", "w") as file:
            file.write("[CLASSIFIED] New security protocols archived")
        with open("preservated.txt", "r") as file:
            print(file.read())
        print("Vault automatically sealed upon completion")
    except (PermissionError, IsADirectoryError, FileNotFoundError) as err:
        print(err)
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
