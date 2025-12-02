
file = "live.txt"

movements_raw =  open(file).read().split(",")
movements = []
for move in movements_raw:
    first_id, last_id = move.split("-")
    movements.append(( int(first_id), int(last_id) ))


def is_invalid_seat_id(seat_id: str) -> bool:
    # print("Checking Seat ID:", seat_id)
    chain_range = range(1, len(seat_id))
    # print("Chain Range:", list(chain_range))
    for index in chain_range:
        substring = seat_id[:index]
        substring_length = int(len(substring))
        # print("  Checking Substring:", substring)
        if substring_length % substring_length != 0:
            # print(int(seat_id), substring_length)
            # print("    Not Divisible, Continuing")
            continue
        
        times_to_repeat = len(seat_id) // substring_length
        # print("    Times to Repeat:", times_to_repeat)
        repeated = substring * times_to_repeat
        # print("    Repeated:", repeated)
        if repeated == seat_id:
            return True
    return False

invalid_ids = set()
for first_id, last_id in movements:
    for seat_id in range(first_id, last_id+1):
        current_id = str(seat_id)
        if is_invalid_seat_id(current_id):
            invalid_ids.add(seat_id)

print("Total Invalid IDs:", sum(invalid_ids))

