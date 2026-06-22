#!/usr/bin/env python3

import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    try:
        valid_ops = {"add": functools.reduce(operator.add, spells),
                     "multiply": functools.reduce(operator.mul, spells),
                     "max": functools.reduce(max, spells),
                     "min": functools.reduce(min, spells)}
        if operation not in valid_ops.keys():
            raise ValueError(f"Operation '{operation}' is invalid")
        if not spells or not len(spells):
            return 0
        return valid_ops[operation]

    except Exception as err:
        raise Exception(f"Spell reducer: {err}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    try:
        if not callable(base_enchantment):
            raise TypeError("Base Enchantment isn't callable")
        functions = {
            "water": functools.partial(base_enchantment, 50, "water"),
            "fire": functools.partial(base_enchantment, 50, "fire"),
            "air": functools.partial(base_enchantment, 50, "air")
        }
    except Exception as err:
        raise Exception(f"partial_enchanter: {err}")

    return functions


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multicast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    spell_powers = [25, 41, 36, 11, 24, 10]
    operations = ["add", "multiply", "max", "min"]
    print("=== Testing spell reducer... ===")
    for op in operations:
        print(f"{op}: {spell_reducer(spell_powers, op)}")

    print("\n=== Testing partial enchanter... ===")

    def enchanter(power: int, element: str, target: str) -> str:
        return f"Pow: {power}, Elem: {element}, target: {target}"

    partialized = partial_enchanter(enchanter)
    print(f"{partialized['water']('Charmander')}\n"
          f"{partialized['fire']('Bulbasaur')}\n"
          f"{partialized['air']('Pikachu')}\n")

    print("\n=== Testing memoized fibonacci... ===")
    print(f"\t{memoized_fibonacci.cache_info()}")
    print(f"{memoized_fibonacci(13)}\n\t{memoized_fibonacci.cache_info()}")
    print(f"{memoized_fibonacci(13)}\n\t{memoized_fibonacci.cache_info()}")
    print(f"{memoized_fibonacci(23)}\n\t{memoized_fibonacci.cache_info()}")
    print(f"{memoized_fibonacci(13)}\n\t{memoized_fibonacci.cache_info()}")

    print("\n=== Testing spell dispatcher... ===")
    dispatch = spell_dispatcher()
    print(f"{dispatch(42)}\n"
          f"{dispatch('fireball')}\n"
          f"{dispatch(['fireball', 'AquaJet', 'Freeze'])}\n"
          f"{dispatch(None)}")
