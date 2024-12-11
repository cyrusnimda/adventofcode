
#file = "demo.txt"
file = "live.txt"

grid =  list(map(list,open(file).read().split("\n")))
#print(grid)

def is_antena_in_position(position : tuple) -> bool:
    return grid[position[0]][position[1]] != "."

# Get all antenas positions
antenas_positions = set()
for x in range(0,len(grid)):
    for y in range(0,len(grid[x])):
        current_position = (x,y)
        if is_antena_in_position(current_position):
            #print(f"Antena in position ({x},{y})")
            antenas_positions.add(current_position)

#print("Antenas coordenates", antenas_positions)

def get_antinodes(antena : tuple, position : tuple) -> list:
    antinodes = []
    diff = (antena[0] - position[0], antena[1] - position[1])
    antinode1 = (antena[0] + diff[0], antena[1] + diff[1])
    antinode2 = (position[0] - diff[0], position[1] - diff[1])
    # antinode1 = (2*antena[0] - position[0], 2*antena[1] - position[1])
    # antinode2 = (2*position[0] - antena[0], 2*position[1] - antena[1])

    if antinode1[0] >= 0 and antinode1[0] < len(grid) and antinode1[1] >= 0 and antinode1[1] < len(grid[0]):
        antinodes.append(antinode1)
    if antinode2[0] >= 0 and antinode2[0] < len(grid) and antinode2[1] >= 0 and antinode2[1] < len(grid[0]):
        antinodes.append(antinode2)
    return antinodes

# Find antinodes
antinodes_positions = set()
for antena in antenas_positions:
    antena_type = grid[antena[0]][antena[1]]
    #print(f"Checking antena in position {antena} for type {antena_type}")
    for x in range(0,len(grid)):
        for y in range(0,len(grid[x])):
            current_position = (x,y)
            current_position_type = grid[current_position[0]][current_position[1]]
            if current_position == antena:
                continue
            if current_position_type != antena_type:
                continue
            #print(f"Checking posible antinode {current_position}")
            antinodes = get_antinodes(antena, current_position)
            for antinode in antinodes:
                #print(f"Antinodes: {antinodes} for antena {antena} and position {current_position}")
                antinodes_positions.add(antinode)

#print("Antinodes coordenates", antinodes_positions)
print("Antinodes count", len(antinodes_positions))