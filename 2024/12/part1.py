
file = "live.txt"
file = "demo.txt"
file = "small.txt"

grid = list(map(list,open(file, "r").read().split()))
print(grid)

# Find all isles, even if they are not connected
isles = {}
for x in range(len(grid)):
    for y in range(len(grid[x])):
        value= grid[x][y]
        if not value in isles:
            isles[value] = set()

        isles[value].add((x,y))
print()
def are_flowers_connected(flower1: tuple, flower2: tuple) -> bool:
    x1, y1 = flower1
    x2, y2 = flower2
    return abs(x1 - x2) + abs(y1 - y2) == 1

def split_isles(flowers: set) -> list:
    # split isles into connected isles

    connected_isles = list()
    for flower in flowers:
        # check if flower is connected to any connected isle
        connected = False
        for connected_isle in connected_isles:
            for connected_flower in connected_isle:
                if are_flowers_connected(flower, connected_flower):
                    connected_isle.add(flower)
                    connected = True
                    break
            if connected:
                break

        if not connected:
            # create new connected isle
            connected_isles.append({flower})
    return connected_isles

def get_price_for_region(connected_isles: list) -> int:
    area = len(connected_isles)
    perimeter = 123
    return area * perimeter

# Split isles into connected isles
total_isles = 0
for isle, coords in isles.items():
    print(isle, coords)
    connected_split_isles = split_isles(coords)
    print(connected_split_isles, "=>", len(connected_split_isles))
    price_for_region = get_price_for_region(connected_split_isles)
    total_isles += len(connected_split_isles)
    print()

# Count total number of isles
print("Total isles:", total_isles)
