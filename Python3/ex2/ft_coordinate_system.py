import math


def dist_calc(coords1, coords2) -> float:
    """
    calculates distanc with this maths formula
    """
    diff: list = []
    i = 0
    while i < 3:
        diff = diff + [coords2[i] - coords1[i]]
        i += 1
    return math.sqrt((diff[0] ** 2) + (diff[1] ** 2) + (diff[2] ** 2))


def get_player_pos() -> tuple[float, float, float] | None:
    coords_str = input("Enter new coordinates as floats in format"
                       "\'x,y,z\':")
    try:
        count: int = 0
        for c in coords_str:
            if c == ",":
                count += 1
        if count != 2:
            raise TypeError
        coords_list = coords_str.split(',')
    except (TypeError, IndexError):
        print("Invalid syntax")
        return None
    try:
        for num in coords_list:
            float(num)
        x, y, z = map(float, coords_list)
        return (x, y, z)
    except ValueError:
        print(f"Error on parameter \'{num}\': could not"
              f" convert string to float: \'{num}\'")
        return None


def game_coords() -> None:
    print("=== Game Coordinate System ===")
    coords: tuple[float, float, float] | None = get_player_pos()
    while not coords:
        coords = get_player_pos()
    centre = (0, 0, 0)
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
    print(f"Distance to centre: {dist_calc(coords, centre):.4f}\n")
    print("Get a second set of coordinates")
    new_coords: tuple[float, float, float] | None = get_player_pos()
    while not new_coords:
        new_coords = get_player_pos()
    print("Distance between the 2 sets of coordinates"
          f" {dist_calc(new_coords, coords):.4f}")


if __name__ == "__main__":
    game_coords()
