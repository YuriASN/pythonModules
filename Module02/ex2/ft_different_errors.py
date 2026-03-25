def garden_operations(operation_number: int) -> int:
    try:
        match operation_number:
            case 0:
                return int("abc")
            case 1:
                return 23/0
            case 2:
                return open("not/found")
            case 3:
                print("this is string plus " + 25)
            case 4:
                print("Operation completed successfully")

    except (TypeError,
            FileNotFoundError,
            ZeroDivisionError,
            ValueError) as display_error:
        raise display_error


def test_error_types() -> None:
    x = 0
    while x < 5:
        print(f"Testing operation {x}...")
        try:
            garden_operations(x)
        except TypeError as display_error:
            print(f"Caught TypeError : {display_error}")
        except FileNotFoundError as display_error:
            print(f"Caught FileNotFoundError : {display_error}")
        except ZeroDivisionError as display_error:
            print(f"Caught ZeroDivisionError : {display_error}")
        except ValueError as display_error:
            print(f"Caught ValueError : {display_error}")
        finally:
            x += 1


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
