
file = "live.txt"

ranges, ids =  open(file).read().split("\n\n")
ranges = [line.split("-") for line in ranges.splitlines()]
ids = ids.splitlines()

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

# check if ids are in any of the ranges
total = 0
for id in ids:
    id_num = int(id)
    for r in merged_ranges:
        if int(r[0]) <= id_num <= int(r[1]):
            total += 1
            break

#print (merged_ranges)
#print (ids)
print("Total IDs in ranges:", total)