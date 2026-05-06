#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    usable = dark_spell_allowed_ingredients()
    check = "INVALID"
    for ing in usable:
        if ing.lower() in ingredients.lower().split():
            check = "VALID"
            break
    return (f"{ingredients} - {check}")
