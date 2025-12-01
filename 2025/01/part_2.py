
file = "live.txt"
current_position = 50

movements =  open(file).read().split("\n")

def move_dial(direction, steps, current_position, password):
    if direction == "R":
        new_position = current_position + steps
    else:
        new_position = current_position - steps

    if new_position <0 or new_position >= 100:
        if direction == "R":
            new_position = new_position - 100
        else:
            new_position = new_position + 100
        
        if new_position != 0 and current_position != 0:
            password += 1

    return new_position, password


password = 0
for move in movements:
    direction = move[0]
    steps = int(move[1:])
    if steps > 100:
        rounds = steps // 100
        steps = steps % 100
        #print (f"Full rounds: {rounds}")
        password += rounds

    current_position, new_password = move_dial(direction, steps, current_position, password)
    password = new_password

    if current_position == 0:
        password += 1
    #print (f"New Position: {current_position}")
    
print(f"Password: {password}")