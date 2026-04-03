#!/usr/bin/env python3

import sys


def safe_int(arg: str) -> int | None:
    try:
        return int(arg)
    except ValueError as err:
        print(err)
        return None


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    scores: list[int] = [x for arg in args if (x := safe_int(arg)) is not None]
    if not scores:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
