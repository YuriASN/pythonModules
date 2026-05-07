#!/usr/bin/env python3

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    return (f"Spell recorded: {spell_name} " +
            f"({validate_ingredients(ingredients)})")
