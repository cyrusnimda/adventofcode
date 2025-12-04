
file = "live.txt"

grid_lines =  open(file).read().split("\n")
grid = [list(map(str, line)) for line in grid_lines]
ROLL_PAPER = "@"

def print_grid(grid: list):
    for line in grid:
        print("".join(line))
    print()

#print_grid(grid)

def get_neighbourgs(coord: tuple, grid: list) -> list:
    x, y = coord
    neighbours = []
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbours.append((nx, ny))
    
    return neighbours

forklift = set()
for x in range(len(grid)):
    for y in range(len(grid[0])):
        rolls_count = 0
        current = grid[x][y]
        if current != ROLL_PAPER:
            continue
        neighbours = get_neighbourgs((x, y), grid)
        for neighbour in neighbours:
            nx, ny = neighbour
            if grid[nx][ny] == ROLL_PAPER:
                rolls_count += 1
        if rolls_count <4:
            forklift.add((x, y))

#print("Positions needing forklifts:", forklift)
print("Total forklifts needed:", len(forklift))