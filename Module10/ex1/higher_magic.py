#!/usr/bin/env python3

from typing import List, Tuple
from collections.abc import Callable


def spell(target: str, power: int) -> str:
    return f"{target} attacked with {power} power"


def heal(target: str, power: int) -> str:
    return f"{target} healed for {power} HP"


def move(target: str, power: int) -> str:
    return f"{target} moved {power} meters"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    if not callable(spell1) or not callable(spell2):
        raise TypeError("Creating spell combiner: "
                        "Both spells must be callable")
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    if not callable(base_spell):
        raise TypeError("Creating power amplifier: "
                        "Base spell must be callable")
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        return "Spell fizzled"

    if not callable(condition) or not callable(spell):
        raise TypeError("Creating conditional caster: "
                        "Spell and condition must be callable")
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> List[str]:
        try:
            results: List[str] = []
            for spell in spells:
                results.append(spell(target, power))
            return results
        except Exception as err:
            raise Exception(f"Casting all spells: {err}")

    if not all(callable(each) for each in spells):
        raise TypeError("Creating spell_sequence: Spell must be callable")
    return cast_all


if __name__ == "__main__":
    try:
        print("=== Combiner ===")
        combined = spell_combiner(move, spell)
        print(combined("Dragon", 5))

        print("\n=== Amplifier ===")
        amplified = power_amplifier(heal, 5)
        print(amplified("Troll", 10))

        print("\n=== Conditional ===")
        conditional_spell = conditional_caster(lambda target, power: power > 5,
                                               heal)
        print(conditional_spell("Whale", 20))
        print(conditional_spell("Whale", 5))

        print("\n=== Sequence ===")
        cast_all = spell_sequence([spell, heal, move])
        print(cast_all("Human", 5))
    except Exception as err:
        print(err)
