import math

#file = "demo.txt"
file = "live.txt"

time, distance = [int(line.split(":")[1].replace(" ", "")) for line in open(file, "r").read().split("\n")]

posible_wins = 0
for hold_time in range(1, time + 1):
    max_distance = (time - hold_time) * hold_time
    if max_distance > distance:
        posible_wins += 1

print(posible_wins)