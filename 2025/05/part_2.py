
file = "live.txt"

ranges, ids =  open(file).read().split("\n\n")
ranges = [line.split("-") for line in ranges.splitlines()]

# sort ranges by their starting value
ranges.sort(key=lambda x: int(x[0]))

# fix overlapping ranges
merged_ranges = []
for current in ranges:
    if not merged_ranges:
        merged_ranges.append(current)
    else:
        last = merged_ranges[-1]
        if int(current[0]) <= int(last[1]) + 1:
            last[1] = str(max(int(last[1]), int(current[1])))
        else:
            merged_ranges.append(current)

total = 0
for range in merged_ranges:
    total__elements_in_range = (int(range[1]) -  int(range[0]) + 1)
    total += total__elements_in_range

print("Total IDs in ranges:", total)