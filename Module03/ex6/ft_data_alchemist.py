#!/usr/bin/env python3


import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players_names: list = ["Alice", "bob", "Charlie", "dylan", "Emma",
                           "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players_names}")
    all_capitalized = [p.capitalize() for p in players_names]
    print(f"New list with all names capitalized: {all_capitalized}")
    p_already_capitalized = [p for p in players_names if p == p.capitalize()]
    print(f"New list of capitalized names only: {p_already_capitalized}")
    print()
    player_data: dict = {p: random.randint(0, 999) for p in all_capitalized}
    print(f"Score dict: {player_data}")
    total_values: int = sum([player_data[name] for name in player_data])
    avg_score = total_values / len(player_data)
    print(f"Score average is {avg_score:.2f}")
    high_scores: dict = {p: player_data[p] for p in player_data
                         if player_data[p] >= round(avg_score)}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()