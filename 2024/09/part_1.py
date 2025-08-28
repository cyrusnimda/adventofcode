import re
import os

#file = "demo.txt"
file = "live.txt"

disk = list(map(int, open(os.path.join(os.path.dirname(__file__), file), "r").read()))
# print(disk)

hard_drive = []
k = 0
for i in range(len(disk)):
    block = disk[i]
    for x in range(block):
        if i % 2 == 0:
            hard_drive.append(str(k))
        else:
            hard_drive.append('.')
    if i % 2 == 0:
        k += 1

# print(hard_drive)

while True:
    first_free_space_position = hard_drive.index('.')
    last_not_free_caracter_position = 0
    for i in range(len(hard_drive)-1, 0, -1):
        if hard_drive[i] != '.':
            last_not_free_caracter_position = i
            break
    # exit if free space is later than last caracter
    if first_free_space_position > last_not_free_caracter_position: break
    hard_drive[first_free_space_position] = hard_drive[last_not_free_caracter_position]
    hard_drive[last_not_free_caracter_position] = '.'


def get_checksum(disk: str) -> int:
    sum = 0
    for i in range(len(disk)):
        if disk[i] == '.': break
        sum += i * int(disk[i])
    return sum

print("Checksum:", get_checksum(hard_drive))