import re

file = "demo.txt"
#file = "live.txt"

disk = list(map(int, open(file, "r").read()))
#print(disk)

# create disk based on block size
id_number = 0
new_disk = []
is_block_time = True
for block in disk:
    if is_block_time==True:
        new_block = str(id_number)
        id_number+=1
        is_block_time = False
    else:
        new_block = '.'
        is_block_time = True
    for i in range(block):
        new_disk.append(new_block)

print(new_disk)
exit()

# sort free space
def swap_last_block(disk : str) -> list:
    # get position of last not "."  caracter
    last_not_free_caracter_position = 0
    for i in range(len(disk)-1, 0, -1):
        if disk[i] != '.':
            last_not_free_caracter_position = i
            break

    first_free_space_position = disk.index('.')

    disk = list(disk)
    # replace first free space with last caracter
    last_caracter = disk[last_not_free_caracter_position]
    disk[first_free_space_position] = last_caracter

    # add free space at the end
    disk[last_not_free_caracter_position] = '.'

    disk = "".join(disk)
    return disk

disk = "".join(new_disk)

def is_disk_defragmented(disk: str) -> bool:
    return re.search(r"^\d+\.+$", disk)


while not is_disk_defragmented(disk):
    disk = swap_last_block(disk)
    #print(disk)


def get_checksum(disk: str) -> int:
    sum = 0
    for i in range(len(disk)):
        if disk[i] == '.': break
        sum += i * int(disk[i])
    return sum

print("Checksum:", get_checksum(disk))