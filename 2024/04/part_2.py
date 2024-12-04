import regex as re

#file = "demo.txt"
file = "live.txt"

words = list(map(list,open(file).read().split("\n")))
#print(words)

total = 0
for x in range(len(words)):
    for y in range(len(words[x])): 
        # we start only from the letter X
        if words[x][y] == "A":
            #print("A found at", x, y)
            if x> 0 and y>0 and y < len(words[x])-1 and x < len(words[x])-1:
                # Get horizontal words
                if words[x+1][y+1] == "S" and words[x+1][y-1] == "S" and words[x-1][y-1] == "M" and words[x-1][y+1] == "M":
                    print("ASMS found at", x, y)
                    total += 1
                if words[x+1][y+1] == "S" and words[x+1][y-1] == "M" and words[x-1][y-1] == "M" and words[x-1][y+1] == "S":
                    print("ASMS found at", x, y)
                    total += 1
                if words[x+1][y+1] == "M" and words[x+1][y-1] == "M" and words[x-1][y-1] == "S" and words[x-1][y+1] == "S":
                    print("ASMS found at", x, y)
                    total += 1
                if words[x+1][y+1] == "M" and words[x+1][y-1] == "S" and words[x-1][y-1] == "S" and words[x-1][y+1] == "M":
                    print("ASMS found at", x, y)
                    total += 1

            

print("total=", total)