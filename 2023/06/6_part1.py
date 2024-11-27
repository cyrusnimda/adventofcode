import math

#file = "demo.txt"
file = "live.txt"

times, distances = [list(map(int, line.split(":")[1].split())) for line in open(file, "r")]
# print(times)
# print(distances)

races = list(zip(times, distances))
print(races)

races_wins = []
for time, distance in races:
    posible_wins = 0
    for hold_time in range(1, time + 1):
        max_distance = (time - hold_time) * hold_time
        if max_distance > distance:
            posible_wins += 1
    races_wins.append(posible_wins)

# print(races_wins)
total_wins = math.prod(races_wins)

print(total_wins)