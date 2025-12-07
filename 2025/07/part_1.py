from collections import deque

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

queue = deque()
queue.append(starting_point)
seen = set([starting_point])
split = 0
            
def add_to_queue(position: tuple[int, int]) -> None:
    x, y = position
    if 0 <= x < width and 0 <= y < height:
        if position not in seen:
            seen.add(position)
            queue.append(position)
            
def parse_neighbors(position: tuple[int, int], grid: list[str], split: int) -> None:
    x, y = position
    element = grid[y][x]
    if element == "^":
        # add split
        split += 1
        # Add elements to the right and left
        add_to_queue((position[0] -1, position[1]))
        add_to_queue((position[0] +1, position[1]))
    else:
        # Add the element below
        add_to_queue((position[0], position[1] +1))
    
    return split


while queue:
    current_position = queue.popleft()
    split = parse_neighbors(current_position, grid, split)

print("Total steps taken:", split)