
#seeds_line, *blocks = open("./demo.txt", "r").read().split("\n\n")
seeds_line, *blocks = open("./real.txt", "r").read().split("\n\n")

seeds = list(map(int,seeds_line.split(":")[1].split()))

seed_groups = []
for index in range(0, len(seeds), 2):
    seed_groups.append((seeds[index], seeds[index] + seeds[index+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        destination, minSource, amount = list(map(int, line.split()))
        maxSource = minSource + amount
        ranges.append((destination, minSource, maxSource))
    
    result = []
    while len(seed_groups) > 0:
        seed_ini, seed_end = seed_groups.pop()
    
        for destination, minSource, maxSource in ranges:
            overlap_start = max(seed_ini, minSource)
            overlap_end = min(seed_end, maxSource)
            if(overlap_start < overlap_end):
                result.append((overlap_start - minSource + destination, overlap_end - minSource + destination))
                if overlap_start > seed_ini:
                    seed_groups.append((seed_ini, overlap_start))
                if overlap_end < seed_end:
                    seed_groups.append((overlap_end, seed_end))
                break
        else:
            result.append((seed_ini, seed_end))

    seed_groups = result

print(min(result)[0])
