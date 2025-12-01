
file = "live.txt"
current_position = 50

movements =  open(file).read().split("\n")
password = 0
#print(movements)
for move in movements:
    direction = move[0]
    steps = int(move[1:])
    if steps > 100:
        steps = steps % 100
    #print(f"Direction: {direction}, Steps: {steps}")
    new_position  = current_position + steps if direction == "R" else current_position - steps
    # check for wrap around
    if new_position >= 100:
        new_position = new_position - 100
    elif new_position < 0:
        new_position = 100 + new_position
    current_position = new_position
    if current_position == 0:
        password += 1
    #print (f"New Position: {current_position}")
    
print(f"Password: {password}")