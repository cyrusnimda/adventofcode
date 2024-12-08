
#file = "demo.txt"
file = "live.txt"

maze =  list(map(list,open(file).read().split("\n")))

def get_guard_initial_position() -> int:
    for x in range(len(maze)):
        if "^" in maze[x]:
            return (x, maze[x].index("^"))

def is_position_osbtacle(position : tuple) -> bool:
    #print("position", position)
    return  maze[position[0]][position[1]] == "#"

def get_next_step() -> tuple:
    #print("current_position", current_position)
    next_step = ()
    if guard_direction == "up":
        next_step =  (-1, 0)
    elif guard_direction == "down":
        next_step =  (1, 0)
    elif guard_direction == "left":
        next_step =  (0, -1)
    elif guard_direction == "right":
        next_step =  (0, 1)
    return (current_position[0] + next_step[0], current_position[1] + next_step[1])
    
def end_of_maze(position) -> bool:
    if position[1] == -1:
        return True
    if position[1] == len(maze):
        return True
    if position[0] == -1:
        return True
    if position[0] == len(maze[0]):
        return True
    return False

def move_guard():
    global current_position
    current_position = get_next_step()

def change_direction():
    global guard_direction
    if guard_direction == "up":
        guard_direction = "right"
    elif guard_direction == "right":
        guard_direction = "down"
    elif guard_direction == "down":
        guard_direction = "left"
    elif guard_direction == "left":
        guard_direction = "up"

def put_obtacle_in_position(position):
    maze[position[0]][position[1]] = "#"

def remove_obtacle_in_position(position):
    maze[position[0]][position[1]] = "."

# get guard visited path patrol
guard_direction = "up"
current_position = get_guard_initial_position()
initial_position = get_guard_initial_position()
position_visited = set()

while True:
    position_visited.add(current_position)
    if end_of_maze(get_next_step()):
        break
    if is_position_osbtacle(get_next_step()):
        change_direction()
    else:
        move_guard()


loops = set()
# fing loops in the guard path patrol
for position in position_visited:
    if position == initial_position:
        continue
    #print("position of obstacle", position)

    put_obtacle_in_position(position)
    guard_direction = "up"
    current_position = get_guard_initial_position()
    position_visited_with_direction = set()

    while True:
        current_position_with_direction = (current_position, guard_direction)
        if(current_position_with_direction in position_visited_with_direction):
            loops.add(position)
            break
        position_visited_with_direction.add(current_position_with_direction)
        if end_of_maze(get_next_step()):
            break
        if is_position_osbtacle(get_next_step()):
            change_direction()
        else:
            move_guard()

    remove_obtacle_in_position(position)

print("total loops", len(loops))