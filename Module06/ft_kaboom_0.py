#!/usr/bin/env python3

from alchemy.grimoire import light_spell_record


def test_light_spell() -> None:
    print("Testing record light spell: "
          f"{light_spell_record("Fantasy", "Fire, wind and snow")}")


if __name__ == "__main__":
    print("=== Kaboom 0 ===\nUsing grimoire module directly")
    test_light_spell()
