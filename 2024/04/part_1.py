import regex as re

#file = "demo.txt"
file = "live.txt"

words = list(map(list,open(file).read().split("\n")))
#print(words)

total = 0
for x in range(len(words)):
    for y in range(len(words[x])): 
        # we start only from the letter X
        if words[x][y] == "X":
            if y < len(words[x])-3:
                # Get horizontal words
                if words[x][y+1] == "M" and words[x][y+2] == "A" and words[x][y+3] == "S":
                    print("XMAS H-> found at", x, y)
                    total += 1

            if y > 2:
                if words[x][y-1] == "M" and words[x][y-2] == "A" and words[x][y-3] == "S":
                    print("SAMX H<- found at", x, y)
                    total += 1

            if x < len(words[x])-3:
                # Get vertical words
                if words[x+1][y] == "M" and words[x+2][y] == "A" and words[x+3][y] == "S":
                    print("XMAS VD found at", x, y)
                    total += 1

            if x > 2:
                if words[x-1][y] == "M" and words[x-2][y] == "A" and words[x-3][y] == "S":
                    print("XMAS VU found at", x, y)
                    total += 1

            if x < len(words[x])-3 and y < len(words[x])-3:
                # Get oblique words
                if words[x+1][y+1] == "M" and words[x+2][y+2] == "A" and words[x+3][y+3] == "S":
                    print("XMAS ODR found at", x, y)
                    total += 1   
            
            if x > 2 and y > 2:
                if words[x-1][y-1] == "M" and words[x-2][y-2] == "A" and words[x-3][y-3] == "S":
                    print("XMAS OUL found at", x, y)
                    total += 1

            if y > 2 and x < len(words[x])-3:
                if words[x+1][y-1] == "M" and words[x+2][y-2] == "A" and words[x+3][y-3] == "S":
                    print("XMAS ODL found at", x, y)
                    total += 1

            if x > 2 and y < len(words[x])-3:  
                if words[x-1][y+1] == "M" and words[x-2][y+2] == "A" and words[x-3][y+3] == "S":
                    print("XMAS OUR found at", x, y)
                    total += 1


print("total=", total)