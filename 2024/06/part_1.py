
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
    

print(maze)
print("initial_position", get_guard_initial_position())

guard_direction = "up"
current_position = get_guard_initial_position()
position_visited = set()

while True:
    position_visited.add(current_position)
    if end_of_maze(get_next_step()):
        break
    if is_position_osbtacle(get_next_step()):
        change_direction()
    else:
        move_guard()
        
print()
print("final_position", current_position)
print("total positions visited", len(position_visited))