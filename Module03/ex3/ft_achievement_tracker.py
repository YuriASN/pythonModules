#!/usr/bin/env python3


import random


def gen_player_achievements(achiev: list, amount: int) -> set:
    """Generates a random set of a `amount` of achievements from `acheiv`"""
    player_achiev = set(random.sample(achiev, amount))
    return player_achiev


def main() -> None:
    """Create 4 players and get statistics about their abillities"""

    all_achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                        'Speed Runner', 'Survivor', 'Master Explorer',
                        'Treasure Hunter', 'Unstoppable', 'First Steps',
                        'Collector Supreme', 'Untouchable', 'Sharp Mind',
                        'Boss Slayer''Untouchable']
    players: list = [
        {"name": "Alice",
         "achievements": gen_player_achievements(all_achievements, 6)},
        {"name": "Bob",
         "achievements": gen_player_achievements(all_achievements, 7)},
        {"name": "Charlie",
         "achievements": gen_player_achievements(all_achievements, 9)},
        {"name": "Dylan",
         "achievements": gen_player_achievements(all_achievements, 5)}
    ]
    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(f"Player {player['name']}: {player['achievements']}")
    all_on_players: set = {achiev for player in players
                           for achiev in player["achievements"]}
    common_achiev = all_on_players
    for player in players:
        common_achiev = set.intersection(common_achiev, player["achievements"])
    print(f"\nAll distinct achievements: {all_on_players}\n")
    print(f"Common achievements: {common_achiev}\n")
    for player in players:
        only_one: set = player["achievements"]
        for p in players:
            if p["name"] == player["name"]:
                continue
            only_one = only_one.difference(p["achievements"])
        print(f"Only {player['name']} has: {only_one}")
    print()
    for player in players:
        missing = set.difference(all_on_players, player['achievements'])
        print(f"{player['name']} is missing: {missing}")


if __name__ == "__main__":
    main()
