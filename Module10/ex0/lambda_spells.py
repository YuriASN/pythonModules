#!/usr/bin/env  python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    artifacts.sort(key=lambda each: each["power"], reverse=True)
    return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = list(map(lambda spell: "*" + spell + "*", spells))
    return transformed


def mage_stats(mages: list[dict]) -> dict:
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    avg_power: float = sum(mage["power"] for mage in mages) / len(mages)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": round(avg_power, 2)
    }


if __name__ == "__main__":
    artifacts = [{"name": "Crystal Orb", "power": 95, "type": "weapon"},
                 {"name": "Ice Wand", "power": 116, "type": "armor"},
                 {"name": "Earth Shield", "power": 100, "type": "armor"},
                 {"name": "Ice Wand", "power": 69, "type": "focus"}]
    mages = [{"name": "Alex", "power": 93, "element": "wind"},
             {"name": "Alex", "power": 81, "element": "fire"},
             {"name": "Sage", "power": 65, "element": "shadow"},
             {"name": "Casey", "power": 97, "element": "light"},
             {"name": "Zara", "power": 92, "element": "fire"}]
    spells = ["tornado", "heal", "darkness", "earthquake"]

    print("=== Artifacts sorted ===")
    for artifact in artifacts:
        print(artifact)
    artifact_sorter(artifacts)
    print("---")
    for artifact in artifacts:
        print(artifact)

    print("\n=== Spells Transformed ===")
    print(spell_transformer(spells))

    print("\n=== Mages Stats ===")
    print(mage_stats(mages))
