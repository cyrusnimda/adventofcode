from collections import deque

#file = "demo.txt"
file = "live.txt"

stones = list(map(int,open(file, "r").read().split()))
blinks = 25
#print(stones)
for blink in range(blinks):
    i = 0
    while i < len(stones):
        value = stones[i]
        # print(i, value)
        str_value = str(value)
        if value == 0:
            stones[i] = 1
        elif len(str_value) % 2 == 0:
            left_stone = str_value[:len(str_value)//2]
            right_stone = str_value[len(str_value)//2:]
            stones[i] = int(left_stone)
            stones.insert(i+1, int(right_stone))
            i += 1
        else:
            stones[i]  = stones[i]  * 2024
        i += 1

    #print(stones)
print("len=", len(stones))
