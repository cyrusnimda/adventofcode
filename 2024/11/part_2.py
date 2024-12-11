from functools import cache

#file = "demo.txt"
file = "live.txt"

stones = list(map(int,open(file, "r").read().split()))

@cache
def process_stone(stone: int, blinks_left: int) -> int:
    if blinks_left == 0: return 1

    if stone == 0:
        return process_stone(1, blinks_left - 1)
    
    str_stone = str(stone)
    lenth = int(len(str_stone))
    if lenth % 2 == 0:
        # print("stone", stone, "lenth",  lenth)
        left_stone = int(str_stone[:lenth//2])
        right_stone = int(str_stone[lenth//2:])
        return process_stone(left_stone, blinks_left - 1) + process_stone(right_stone, blinks_left - 1)
    else:
        return process_stone(stone * 2024, blinks_left - 1)

total = 0
for stone in stones:
    total += process_stone(stone, 75)

print(total)