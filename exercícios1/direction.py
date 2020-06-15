def dirReduc(arr):
    a = arr.count("NORTH")
    b = arr.count("SOUTH")
    c = arr.count("WEST")
    d = arr.count("EAST")
    directions = []
    if a - b != 0:
        if a - b > 0:
            (a - b) * directions.append(['NORTH'])
        else:
            (b - a) * directions.append(['SOUTH'])
    if c - d != 0:
        if c - d > 0:
            (c - d) * directions.append(['WEST'])
        else:
            (d - c) * directions.append(['EAST'])
    else:
        return arr

    return directions

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
