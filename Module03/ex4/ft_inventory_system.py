#!/usr/bin/env python3


import sys


class InventoryError(Exception):
    pass


class DoubleItemError(InventoryError):
    def __init__(self, key: str = "unknown") -> None:
        super().__init__(f"Redundant item '{key}'- discarding")


class ParameterError(InventoryError):
    def __init__(self, param: str = "unknown") -> None:
        super().__init__(f"Error - invalid parameter '{param}'")


class AmountError(InventoryError):
    def __init__(self, param: str = "unknown", value: int = 0) -> None:
        super().__init__(f"Value {value} for {param} is invalid")


def safe_inventory_add(inventory: dict, key: str, value: str) -> None:
    """Checks if the key exists in the inventory before adding
    in order to avoid change of values on existing keys"""

    if key in inventory:
        raise DoubleItemError(key)
    amount = int(value)
    if amount < 1:
        raise AmountError(key, amount)
    inventory[key] = amount


def check_parameter(param: str) -> None:
    if param.count(":") != 1:
        raise ParameterError(param)


def get_inventory(args: list[str]) -> dict:
    """Transforms the arguments into keys and values
    to return the inventory dict"""

    inventory: dict = {}
    for arg in args:
        try:
            check_parameter(arg)
            name, value = arg.split(":")
            safe_inventory_add(inventory, name, value)
        except (ValueError, AmountError) as err:
            print(f"Quantity error for '{name}': {err}")
        except ParameterError as err:
            print(err)
        except DoubleItemError as err:
            print(err)
    return inventory


def main() -> None:
    """Runs the program"""
    print("=== Inventory System Analysis ===")
    inventory: dict = {}
    inventory = get_inventory(sys.argv[1:])
    total_itens = len(inventory)
    total_values = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {total_itens} items: "
          f"{total_values}")
    highest: int = 0
    lowest: int = 9999999
    for item in inventory.keys():
        if inventory[item] < lowest:
            lowest = inventory[item]
        if inventory[item] > highest:
            highest = inventory[item]
        print(f"Item {item} represents "
              f"{inventory[item] / total_values * 100:.1f}%")
    for item in inventory:
        if inventory[item] == highest:
            print(f"Item most abundant: {item} with quantity {highest}")
            break
    for item in inventory:
        if inventory[item] == lowest:
            print(f"Item most abundant: {item} with quantity {lowest}")
            break
    inventory["new_item"] = 20
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
