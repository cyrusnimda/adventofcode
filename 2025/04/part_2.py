
file = "live.txt"

grid_lines =  open(file).read().split("\n")
grid = [list(map(str, line)) for line in grid_lines]
ROLL_PAPER = "@"
EMPTY = "."

def print_grid(grid: list):
    for line in grid:
        print("".join(line))
    print()


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


def get_forklifts(grid: list) -> set:
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
    return forklift

rolls_removed = 0
while len(get_forklifts(grid)) > 0:
    forklift = get_forklifts(grid)
    rolls_removed += len(forklift)
    for x, y in forklift:
        grid[x][y] = EMPTY


#print("Positions needing forklifts:", forklift)
print("Total forklifts removed:", rolls_removed)