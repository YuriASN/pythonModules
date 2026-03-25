#!/usr/bin/env python3

import sys
import os

sys.dont_write_bytecode = True

EXERCISES = {
    "0": (0, ["ft_hello_garden"]),
    "1": (1, ["ft_garden_name"]),
    "2": (2, ["ft_plot_area"]),
    "3": (3, ["ft_harvest_total"]),
    "4": (4, ["ft_plant_age"]),
    "5": (5, ["ft_water_reminder"]),
    "6": (6, ["ft_count_harvest_iterative", "ft_count_harvest_recursive"]),
    "7": (7, ["ft_seed_inventory"]),
}


def test_ft_exercise(exercise_file_name, exercise_number):

    print(f"\n=== Testing {exercise_file_name} ===")

    exercise_folder = os.path.join(
        os.path.dirname(__file__), f"ex{exercise_number}"
    )

    original_path = list(sys.path)

    try:
        sys.path.insert(0, exercise_folder)

        module = __import__(exercise_file_name)

        function = getattr(module, exercise_file_name)

        if exercise_file_name == "ft_seed_inventory":

            print("Testing with different seed types and units:\n")

            function("tomato", 15, "packets")
            function("carrot", 8, "grams")
            function("lettuce", 12, "area")

            print("\nTesting with unknown unit:")
            function("basil", 5, "unknown")

        else:
            function()

    except ImportError:
        print(f"❌ No {exercise_file_name}.py in ex{exercise_number}")

    except AttributeError:
        print(
            f"❌ Could not find function {exercise_file_name}() "
            f"in {exercise_file_name}.py"
        )

    except Exception as error:
        print(f"❌ Error running your function: {error}")

    finally:
        sys.path = original_path


def print_menu():

    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.\n")

    print("0 - ft_hello_garden")
    print("1 - ft_garden_name")
    print("2 - ft_plot_area")
    print("3 - ft_harvest_total")
    print("4 - ft_plant_age")
    print("5 - ft_water_reminder")
    print("6 - ft_count_harvest")
    print("7 - ft_seed_inventory")
    print("a - test all exercises\n")


def run_exercise(choice):

    exercise_number, files = EXERCISES[choice]

    for file in files:
        test_ft_exercise(file, exercise_number)


def main():

    print_menu()

    choice = input("Enter your choice: ")

    if choice == "a":

        for key in EXERCISES:
            run_exercise(key)

    elif choice in EXERCISES:

        run_exercise(choice)

    else:

        print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
