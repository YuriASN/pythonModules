#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Kaboom 1 ===\n"
          "Access to alchemy/grimoire/dark_spellbook.py directly\n"
          "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print("Testing record dark spell: "
          f"{dark_spell_record("Fantasy", "Earth, wind and fire")}")
