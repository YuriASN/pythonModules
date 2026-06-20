#!/usr/bin/env python3


def words_only(string: str) -> list[str]:
    words: list[str] = []
    current: str = ""

    for char in string:
        if char.isalpha():
            current += char
        elif current:
            words.append(current)
            current = ""
    print(words)
    return words


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    usable = light_spell_allowed_ingredients()
    for word in usable:
        word = word.lower()
    check = "VALID"
    for word in words_only(ingredients):
        if word.lower() not in usable:
            check = "INVALID"
            break
    return (f"{ingredients} - {check}")
