#!/usr/bin/env python3

from typing import Callable, Any, Dict


def mage_counter() -> Callable:
    counter = 0

    def add_count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return add_count


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate(power_add: int) -> int:
        nonlocal initial_power
        initial_power += power_add
        return initial_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    data: Dict[str, Callable] = {}

    def store(key: Any, value: Any):
        nonlocal data
        data[key] = value

    def recall(key: str) -> Any:
        nonlocal data
        if key in data.keys():
            return data[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    try:
        print("=== Mage Counter ===")
        counter = mage_counter()
        counter2 = mage_counter()
        for _ in range(3):
            print(f"Counter: {counter()}")
        print("Using both counters:")
        for _ in range(2):
            print(f"Counter:\t{counter()}")
            print(f"Counter2:\t{counter2()}")

        print("\n=== Spell Accumulator ===")
        accumulator = spell_accumulator(9)
        for _ in range(5):
            print(f"After add 3: {accumulator(3)}")

        print("\n=== Enchantment ===")
        slayer = enchantment_factory("Slaying")
        healer = enchantment_factory("Healing")
        print(f"Enchanting 'sword': {slayer('sword')}\n"
              f"Enchanting 'keyboard': {healer('keyboard')}")

        print("\n=== Memory Vault ===")
        safe_data = memory_vault()
        print(safe_data["recall"]("school"))
        safe_data["store"]("school", 42)
        print(safe_data["recall"]("school"))

    except Exception as err:
        print(err)
