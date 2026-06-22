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
            "water": functools.partial(base_enchantment(power=50,
                                                        element="water")),
            "fire": functools.partial(base_enchantment(power=50,
                                                       element="fire")),
            "air": functools.partial(base_enchantment(power=50, element="air"))
        }
    except Exception as err:
        raise Exception(f"partial_enchanter: {err}")

    return functions


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def spell_dispatcher(spell: Any) -> Callable[[Any], str]:
    return lambda spell: "Unknown spell type"


@spell_dispatcher
def _(spell: int) -> str:
    return f"Damage spell: {spell} damage"


@spell_dispatcher
def _(spell: str) -> str:
    return f"Enchantment: {spell}"


@spell_dispatcher
def _(spell: list) -> str:
    return f"Multicast: {len(spell)} spells"


if __name__ == "__main__":
    spell_powers = [25, 41, 36, 11, 24, 10]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [8, 20, 13]
    print("=== Testing spell reducer... ===")
    print("=== Testing partial enchanter... ===")
    print("=== Testing memoized fibonacci... ===")
    print("=== Testing spell dispatcher... ===")
