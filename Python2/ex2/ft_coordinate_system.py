import sys
import math

def distance(coords):
    return math.sqrt((coords[0] ** 2) + (coords[1] ** 2) + (coords[2] ** 2))
    
print("=== Game Coordinate System ===")
args = sys.argv
try:
    try:
        int(args[4])
        print("Too many coordinates were given, only 3 coordinates can be accepted")
    except:
        pass
    coords = (int(args[1]), int(args[2]), int(args[3]))
    print(f"Position created: {coords}")
except:
    try:
        temp = args[1].split(',')
        i = 0
        try:
            while i < 3:
                temp[i] = int(temp[i])
                i += 1
            try:
                temp[3]
                temp = []
                print("Too many coordinates were given, only 3 coordinates can be accepted")
            except:
                pass
        except:
            try:
                temp[i]
                print(f"Parsing invalid cooridnates \"{args[1]}\"")
                print(f"Error parsing coordinates: invalid literal for int() with base 10: '{temp[i]}'")
                print(f"Error details - Type: ValueError, Args: (\"invalid literal for int() with base 10: '{temp[i]}\",)")
            except:
                print("Not enough coordinates were given, only 3 coordinates can be accepted")
            temp = []
        coords = tuple(temp)
        if not coords == ():
            print(f"Parsing coordinates: \"{args[1]}\"")
            print(f"Parsed position: {coords}")
    except:
        try:
            args[1]
        except:
            print("No arguments present")
try:
    print(f"Distance between (0, 0, 0) and {coords}: {distance(coords):.2f}")
except:
    pass