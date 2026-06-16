#!/usr/bin/env python3


def secure_archive(file_name: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    """
    Read or write to 'file_name' accordlingly to the action received.

    Args:
        file_name: File to work with.
        action: 'r' for read and 'w' for write.
        content: String to write to file in case of action being 'w'.
    """
    try:
        if action == "r" or "w":
            with open(file_name, action) as opened:
                if action == "r":
                    return (True, opened.read())
                else:
                    opened.write(content)
                    return (True, 'Content successfully written to file')
        else:
            return (False, 'Action to perform isn\'t \'r\' or \'w\'')
    except Exception as err:
        return (False, f'{err}')


if __name__ == "__main__":
    try:
        print("=== Cyber Archives Security ===\n")
        print("Using 'secure_archive' to read from a nonexistent file:\n"
              f"{secure_archive('not/existing/file', 'r')}")
        print()
        print("Using 'secure_archive' to read from an inaccessible file:\n"
              f"{secure_archive('perm.txt', 'r')}")
        print()
        readed = secure_archive("data.txt", "r")
        print("Using 'secure_archive' to read from a regular file:\n"
              f"{readed}")
        print()
        print("Using 'secure_archive' to write previous content to a new "
              f"file:\n{secure_archive('newex3', 'w', readed[1])}")
    except Exception as err:
        print(err)
