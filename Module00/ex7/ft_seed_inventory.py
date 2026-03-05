def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.lower()
    seed_type = seed_type[0].upper() + seed_type[1:]
    unit = unit.lower()
    if unit == "packets":
        print(seed_type + " seeds: ", end='')
        print(quantity, end=' ')
        print("packets available")
    elif unit == "grams":
        print(seed_type + " seeds: ", end='')
        print(quantity, end=' ')
        print("grams total")
    elif unit == "area":
        print(seed_type + " seeds: covers ", end='')
        print(quantity, end=' ')
        print("square meters")
    else:
        print("Unknown unit type")
