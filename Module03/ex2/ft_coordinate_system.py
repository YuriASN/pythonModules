#!/usr/bin/env python3

import math


def get_player_pos() -> tuple:
    while True:
        coordenates = [point.strip() for point in input(
            "Enter new coordinates as floats "
            "in format 'x, y, z': ").split(',')]
        if len(coordenates) != 3:
            print("Invalid sintax")
            continue
        values: list[int] = []
        for point in coordenates:
            try:
                values.append(float(point))
            except ValueError as err:
                print(f"Error on parameter '{point}': {err}")
                break
        else:
            return tuple(values)


def distance_3d(x1: float, y1: float, z1: float,
                x2: float, y2: float, z2: float) -> float:
    distance: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos_1 = get_player_pos()
    print(f"Got a first tuple: {pos_1}")
    print(f"It includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
    print(f"Distance to center: {distance_3d(*pos_1, 0, 0, 0):.4f}\n")

    print("Get a first set of coordinates")
    pos_2 = get_player_pos()
    print(f"Got a second tuple: {pos_1}")
    print(f"It includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_3d(*pos_1, *pos_2):.4f}")


if __name__ == "__main__":
    main()
