#! /usr/bin/env python3

from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                if min_power > args[2]:
                    return "Insufficient power for this spell"
                return func(*args, **kwargs)
            except KeyError as err:
                print(f"Validating power keyword error: {err}")

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            curr_exception: Exception | None = None
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if i + 1 < max_attempts:
                        print("Spell failed, retying... "
                              f"(attempt {i + 1}/{max_attempts})")
                    curr_exception = err
            if curr_exception is not None:
                return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3 and all(c.isalpha() or c.isspace() for c in name):
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("=== Testing spell timer ===")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.321)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\n=== Testing retrying spell ===")

    @retry_spell(4)
    def hadouken_cast(power: int) -> str:
        if power < 10:
            raise ValueError(f"Power ({power}) too low")
        return "Hadouken spelled!"

    print(hadouken_cast(9))
    print("---")
    print(hadouken_cast(20))

    print("\n=== Testing MageGuild ===")
    mage = MageGuild()
    print(
        f"{mage.validate_mage_name('xD')}\n{mage.validate_mage_name('Dobby')}"
        f"\n{mage.cast_spell('lightining', 15)}\n"
        f"{mage.cast_spell('lightining', 9)}"
        )
