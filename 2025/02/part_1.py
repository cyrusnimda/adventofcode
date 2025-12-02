
file = "live.txt"

movements_raw =  open(file).read().split(",")
movements = []
for move in movements_raw:
    first_id, last_id = move.split("-")
    movements.append(( int(first_id), int(last_id) ))

invalid_ids = set()
for first_id, last_id in movements:
    for seat_id in range(first_id, last_id + 1):
        current_id = str(seat_id)
        # check is even number
        if len(current_id) % 2 !=0:
            continue
        half_length = len(current_id) // 2
        left_half = current_id[:half_length]
        right_half = current_id[half_length:]
        if left_half == right_half:
            invalid_ids.add(seat_id)
        #print(f"Invalid Seat ID: {current_id}")
    #exit()

#print("Invalid IDs:", invalid_ids)

print("Total Invalid IDs:", sum(invalid_ids))
