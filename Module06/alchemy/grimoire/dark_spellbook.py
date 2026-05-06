#!/usr/bin/env python3

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return (f"Spell recorded: {spell_name} " +
            f"({validate_ingredients(ingredients)})")
