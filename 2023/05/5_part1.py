
seeds_line, *blocks = open("./demo.txt", "r").read().split("\n\n")
# seeds_line, *blocks = open("./real.txt", "r").read().split("\n\n")

seeds = list(map(int,seeds_line.split(":")[1].split()))
print(seeds)

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        destination, minSource, amount = list(map(int, line.split()))
        maxSource = minSource + amount
        ranges.append((destination, minSource, maxSource))
    
    print("Ranges: " + str(ranges))
    result = []
    for seed in seeds:
        for destination, minSource, maxSource in ranges:
            if minSource <= seed < maxSource:
                result.append(seed - minSource + destination)
                break
        else:
            result.append(seed)

    seeds = result

print("The min seed is " + str(min(result)))
