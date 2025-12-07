from functools  import cache

file = "live.txt"

grid = open(file).read().split("\n")
height = len(grid)
width = len(grid[0])

def get_starting_position(grid: list[str]) -> tuple[int, int]:
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "S":
                return (x, y)
            
starting_point = get_starting_position(grid)
print("Starting position - X:", starting_point[0], "Y:", starting_point[1])


@cache
def get_score(position: tuple[int, int]) -> int:
    x, y = position
    if not (0 <= x < width and 0 <= y < height):
        return 1
    
    element = grid[y][x]
    if element == "^":
        return get_score((position[0] -1, position[1])) + get_score((position[0] +1, position[1]))
    else:
        return get_score((position[0], position[1] +1))

score =get_score(starting_point)
print("Total score:", score)