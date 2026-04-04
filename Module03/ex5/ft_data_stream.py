#!/usr/bin/env python3


import typing
import random


def gen_event() -> typing.Generator[tuple, None, None]:
    """Generates a random player doing an action"""

    name: list = ["alice", "bob", "dylan", "charlie"]
    action: list = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
                    "release"]
    while True:
        yield (random.choice(name), random.choice(action))


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple,
                                                                     None,
                                                                     None]:
    """Removes one event from the list and yields it"""
    while len(events):
        pick = random.choice(events)
        i: int = 0
        for event in events:
            if event == pick:
                del events[i]
                break
            i += 1
        yield pick


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for i in range(1000):
        name, action = next(event)
        print(f"Event {i}: Player {name} did action {action}")
    ten_events: list = [next(event) for i in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    for each in consume_event(ten_events):
        print(f"Got event from list: {each}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
