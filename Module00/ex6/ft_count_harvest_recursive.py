def ft_count_harvest_recursive() -> None:
    def add_up(days, current) -> None:
        if current <= days:
            print("Day ", end='')
            print(current)
            add_up(days, current + 1)
        if current == days:
            print("Harvest time!")
    days = int(input("Days until harvest: "))
    current = 1
    add_up(days, current)
